import pyautogui
import time
import random

count = int(input("input jumlah chat : "))
delay = int(input("input delay : "))
 
print("⏳ Starting bot in 5 seconds...")

for i in range(5, 0, -1):
    print(f"{i}...")
    time.sleep(1)

print("✅ Bot started!")

chats = [
    "What are the key differences between proof-of-work and proof-of-stake consensus mechanisms, and how do they impact the environmental sustainability of blockchain networks?",
    "How has the adoption of layer-2 scaling solutions like Lightning Network and Polygon influenced the transaction speed and cost efficiency of major cryptocurrencies such as Bitcoin and Ethereum?",
    "In what ways could central bank digital currencies (CBDCs) potentially disrupt or coexist with decentralized cryptocurrencies like Bitcoin?",
    "Explain the role of smart contracts in decentralized finance (DeFi) protocols, and discuss potential risks such as flash loan attacks.",
    "How do non-fungible tokens (NFTs) leverage blockchain technology to ensure ownership and provenance, and what are the current challenges in their market adoption?",
    "What are the implications of quantum computing advancements on the security of cryptographic algorithms used in cryptocurrencies?",
    "Analyze the economic factors that contribute to cryptocurrency market volatility, including the influence of institutional investors and macroeconomic events.",
    "How do decentralized autonomous organizations (DAOs) function, and what governance models have proven most effective in real-world applications?",
    "Discuss the regulatory landscape for cryptocurrencies in major economies like the US, EU, and China, and predict potential future developments.",
    "What is the significance of tokenomics in the success of a cryptocurrency project, and how can poor token design lead to failure?",
    "Explore the integration of blockchain technology in supply chain management, including examples from industries like food traceability or pharmaceuticals.",
    "How do privacy-focused cryptocurrencies like Monero or Zcash achieve anonymity, and what are the trade-offs compared to transparent blockchains like Bitcoin?",
    "What role do oracles play in bridging real-world data to blockchain smart contracts, and what are the vulnerabilities in oracle systems?",
    "Analyze the potential of Web3 in transforming social media platforms, including ownership of user data and content monetization.",
    "How has the rise of stablecoins like USDT and USDC affected the liquidity and stability of the broader crypto ecosystem?",
    "Discuss the ethical considerations in cryptocurrency mining, particularly regarding energy consumption and geographic centralization.",
    "What are the key innovations in cross-chain interoperability protocols, such as Polkadot or Cosmos, and how do they address the silos in blockchain ecosystems?",
    "Evaluate the impact of decentralized exchanges (DEXs) on traditional finance, including advantages over centralized exchanges (CEXs) like Binance.",
    "How might blockchain technology evolve to support mass adoption in emerging markets, such as remittances or microfinance in developing countries?",
    "Predict the long-term effects of the Ethereum merge to proof-of-stake on the overall cryptocurrency market, including competition from other layer-1 blockchains.",
    "Stablecoin minting spikes—what’s the one signal that shows market panic’s over, and why?",
    "What’s the oddest Web3 opinion you hold that no one agrees with, and why’s it your hill to die on?",
    "How do you see Web3 redefining friendships, and what’s the glue that binds?",
    "If Hub.xyz’s Dataminer made real-time data free, what’s the one app you’d build, and why’s it revolutionary?",
    "What’s your Web3 opinion on time's value, and why’s it a paradigm shift?",
    "What’s the oddest Web3 opinion you hold that no one agrees with, and why’s it your hill to die on?",
    "What’s the one data stream Hub.xyz could unlock for AI devs, and why’s it a training goldmine?",
    "What’s the oddest Web3 opinion you hold that no one agrees with, and why’s it your hill to die on?",
    "What are the pros and cons of using Binance for crypto trading?",
    "How does binance's fee structure compare to other exchanges?",
    "Which exchange support a wide range of alt coin ?",
    "What is the process for executing trades on decentralized OTC platforms?",
    "What are the benefits of integrating with various blockchains in decentralized exchanges?",
    "What is the impact of native tokens on transaction fees in decentralized exchanges?",
    "What are the steps to activate referral benefits in crypto trading platforms?",
    "How do V2 beta versions address user feedback in trading platforms?",
    "What are the key differences between pre-market and OTC markets in crypto trading?",
    "How do staking mechanisms incentivize platform participation in decentralized finance?",
    "How do referral programs work in decentralized crypto trading platforms?",
    "Which Samsung washing machines have the fastest wash cycles?",
    "How does Samsung's Galaxy Buds3 Pro compare to AirPods Pro?",
    "How does Samsung's Galaxy Watch8 compare to Fitbit Sense?",
    "How to ensure a secure online shopping experience for cosmetics?",
    "What factors contribute to a positive online shopping experience for beauty products?",
    "What programs assist in quitting Marlboro cigarette use?",
    "What regulations govern the production and sale of Marlboro cigarettes?"
]

for i in range(count):
    msg = random.choice(chats)

    pyautogui.click(764, 909)      
    pyautogui.write(msg, interval=0.05)  
    time.sleep(1)

    pyautogui.click(1443, 973)     
    time.sleep(delay)  

