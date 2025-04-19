from masumi.payment import Payment, Amount
from masumi.config import Config
import os
import ast 
import json 

def safe_parse(raw_string):
    try:
        return json.loads(raw_string)
    except json.JSONDecodeError:
        try:
            return ast.literal_eval(raw_string)
        except Exception:
            raise ValueError("⚠️ Could not parse output as JSON or Python literal.")
        


async def pay(result, selected_option): 
    # Payment configuration
    payment_config = Config(
        payment_service_url=os.getenv("PAYMENT_SERVICE_URL"),
        payment_api_key=os.getenv("PAYMENT_API_KEY")
    )

    try:
        cleaned_result = safe_parse(result.strip())
    except Exception as e:
        print("❌ Could not parse structured input from agent.")
        print("⚠️ Agent returned:", result)
        raise e
    
    agent_identifier = os.getenv("AGENT_IDENTIFIER")

    # Simulate input data being submitted for the selected task
    task_input = {
        "text": f"Deploy using strategy {selected_option.upper()}"
    }

    # Define payment amount
    payment_amount = cleaned_result[selected_option]['monthly_price']
    payment_unit = os.getenv("PAYMENT_UNIT", "USD")
    amounts = [Amount(amount=payment_amount, unit=payment_unit)]

    # Purchaser ID could be user-provided or simulated
    purchaser_id = input("🔑 Enter your purchaser identifier (e.g., user123): ")

    # Create payment object
    payment = Payment(
        agent_identifier=agent_identifier,
        config=payment_config,
        identifier_from_purchaser=purchaser_id,
        input_data=task_input
    )

    print("💸 Creating payment request via Masumi...")
    payment_request = await payment.create_payment_request()
    payment_id = payment_request["data"]["blockchainIdentifier"]

    print(f"\n🧾 Payment Request Created:\n- Blockchain ID: {payment_id}\n- Unlock Time: {payment_request['data']['unlockTime']}")
    print("✅ Please complete the payment via your connected wallet.")

    # Wait for payment confirmation
    async def confirm_payment():
        print("⏳ Waiting for payment confirmation on-chain...")
        await payment.start_status_monitoring(lambda pid: print(f"✅ Payment {pid} confirmed!"))
        await payment.complete_payment(payment_id, {"status": "confirmed", "deployment": selected_option})

    await confirm_payment()