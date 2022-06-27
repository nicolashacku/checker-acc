import requests
import os
import json
from colorama import Fore, init
from time import sleep
os.system("cls")
init()
v = Fore.LIGHTGREEN_EX
r = Fore.LIGHTRED_EX
w = Fore.LIGHTWHITE_EX
c = Fore.LIGHTCYAN_EX
b = Fore.BLUE
m = Fore.LIGHTMAGENTA_EX

banner = f'''
{v}
  /$$$$$$  /$$   /$$ /$$$$$$$$  /$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$
 /$$__  $$| $$  | $$| $$_____/ /$$__  $$| $$  /$$/| $$_____/| $$__  $$
| $$  \__/| $$  | $$| $$      | $$  \__/| $$ /$$/ | $$      | $$  \ $$
| $$      | $$$$$$$$| $$$$$   | $$      | $$$$$/  | $$$$$   | $$$$$$$/
| $$      | $$__  $$| $$__/   | $$      | $$  $$  | $$__/   | $$__  $$
| $$    $$| $$  | $$| $$      | $$    $$| $$\  $$ | $$      | $$  \ $$
|  $$$$$$/| $$  | $$| $$$$$$$$|  $$$$$$/| $$ \  $$| $$$$$$$$| $$  | $$
 \______/ |__/  |__/|________/ \______/ |__/  \__/|________/|__/  |__/

{c}Checker Desarrollado por nicolas.$
'''


def checker():
    os.system("cls")
    print(banner)
    correo = str(input("Digite el correo a comprobar: "))
    password = str(input("Digite la contraseña del correo: "))
    ####disney


    headers_ds = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Authorization': 'eyJ6aXAiOiJERUYiLCJraWQiOiJ0Vy10M2ZQUTJEN2Q0YlBWTU1rSkd4dkJlZ0ZXQkdXek5KcFFtOGRJMWYwIiwiY3R5IjoiSldUIiwiZW5jIjoiQzIwUCIsImFsZyI6ImRpciJ9..Q_uRKKf2K_UEuwEV.Xp8j2qoC5Cp0loypFIgUg-AjaYqixzE2lS82IWDZvo7KAY6r6ixKS7QL-Lx7ZhFp3SHCUyRTDjbXIwEMDKxDh3pwPwX7UfCoz6vLBa0YhtGyi9l1fnb0oMtIyJHBTDEYRyqvFTrt0GW0qIpjLnUnqZZdf7O8Dl4WoWW9CTtoKNjrbsCpagSBftJ8gedcGoSGHx58qWms-as5-0QE-zUobznpQG9dY4pEPCFC6bQTsDhB6oVGvvDuoOaf8AdV0FWey-d65Ox7S_-3PxE046hz2XI6axoZsR416HFLLrGCkkZ1PW05OztiEGe6D5DEQyjJeu-GazTBnPqVR_wI2RaQ5SPzE4BqX8XZziN6Yp4oDKTKpGPJo-X6e6SCDPdgy3TF4N6aRXDvP_zn-k0NZV6g0OoD0SJTDU4tFksiOpyCUqTCIeZ5KD-wcWzcx7JdOoKdSLNMtFTddQfdpu5pNOegPP306mQ0yzwBhwZxqmnXK_nF81CIgzcn9DSxxvdlBFobqV9dWOcfhD5DFzEoAjNOMwRO8V0kPTGHoM_kO5uhT3i7mvgnf4EbROTvmV5aCeYBm3u7ahEL7hqQJh1sNKmfseWmFaR81BbAppgGaygTHnlk4ASPSReVr5QH1JHGsvRH-f2cgwHTFC3-EzKVhjZfiuaZk2EaW_aTDrn9_cLlGMjQ_BhgxpzZ2YO-sItOxMpsiXzNx3m9EBeC11lw9FuGsh800n5WbAnRib67ht2xCL0pu8wpILS3Rk8usMA96KGYmZ59EBlplGJrmgixr4x_HSvdT_79jKM7obMKa0Zk1twVxqqDBabqvDH2aL8ufbg2FiHjYwG_o1U1VK4bXKKmpY4FtaLMfj6Zwhu7ab4DS7a_E9FUtmiw8JiET6YjI4qnpTanqpFj9pgtC9DeWRrZY-F5FGRij6BM3n6grQl6hCkJu03xd-iOodV-SujXyopeAXg_S4ETGNDax53iAYyb5jaeM7sTbOKO-O0K_4RwgNxpWDRAvBQDPdm8mAGkjBmWixc_1sxA7iay9zj1PV5NuY7HO908PruthnZXw5t-naX_d90SxqqaWHHDkZdzmxjLmaCFqJQREcrrgVhAjSYzUy4TYFxWbmAxV5N6Xt0PVyWd0z2GcxGVfGuSgkuSmNiwIRVLOeYYB4OZ8UI-a9a_XrR9Oe_WhEmh1XVd1ZkZ5Zs45gjP4zQW0UrZEslqhThVxa9SxHzl99skub0syfdThNGO6ZmjzRGsUyRumO4y4CXf3MxRHfuGloR4PtVOlu8GBjW1X0AnMYKHg_l0WGSYIz8l_W7eYao5TMD7_yR6ZNicNKrzKVE2jzCMt7SfYX4HUtkVgiabS1ETahoEoVraWf_qtS7Of3DGeskkC7Isfz6IcKTl-aei3VwfyiLnnqyf6LuFHxPi3Hpcpbsn0dUaEfqjV9EVmZw4lV4IkS29Op0fBmrWgo5BPX4yiSjM58KX1oyfVu6C70Mo51_7zq9oyYXYp535GFcmmkoapVRmeVFncsrxAUlVcPd1i12EpsBRbB6lXoxF_T-HEWiJa1Px26Orc03SDHefltKdTrBZF3jk2g1_pxNzcoM9312fEgdagVwLyWRoLusTfk0-uWw5By9XefQ2jjFfTHf5dVlIbV9TYsl_PPzg_XJLOx0mDAdfwbC1I0m8WsZxbKkrdY3eKDyu2FBO7Wiyjx0YThiunt8vWfFO7RFppZU2ILJxtqNy7p5fm9plpCCnlRAq4MGu8TEbulC4EYVLcCfo7jin5fgW7WyBG5LR-NXk2y10tCmltHhfeZKu7fqW6W9IP7ZdducGLeNYD3YyVthVll6puOPJf-AK6fI9P4i-NplvXLAozwvpWYub11vv_Zv1GVyzXsjnr90Fzdh1AvD1vCPAlGeXZq9Ji0DPJTdHilcP28X0bHpLnijh5juyBm0k3vbe7xAGnxXWgWdS9t1NY3IHGpmN5uTXKIL2pJLStbaFgK4L0BIPFMGjOHARxUP2t3SiRg1DozOnfvjXvMbMnyBFsd5OW3WlgZin_XRVTfjfiUl4dUCjVDT3Beg43R6ZKJDN83ZmlgbM0YJosVrOf0l34kf64RpvwT6Dd0uYS2MOF2QQhuhdSsXnDC-y2R8W2TDgrU0So1gvVDozQk7IggbV3DM9MkiDCvdjLwfxRLnrNFH9uPdCBcql62eyYBQeYeJZfBCa0_n86QpZV89_sjMcS683CzRdoWXpk1a4kDKlNRoByTShLdBOyj9dtwe-IVwzS_iLQj-TIVuKEZhpR5KDgYFYetyZ0Mo74bW9EJ7HvCGcvg.3qxSSFWfB6UOiP3tDo2OiQ',
        'Content-Type': 'application/json'
    }
    json_data_ds = {
        'query': '\n    mutation login($input: LoginInput!) {\n        login(login: $input) {\n            account {\n                ...account\n\n                profiles {\n                    ...profile\n                }\n            }\n            identity {\n                ...identity\n            }\n            actionGrant\n        }\n    }\n\n    \nfragment identity on Identity {\n    attributes {\n        securityFlagged\n        createdAt\n        passwordResetRequired\n    }\n    flows {\n        marketingPreferences {\n            eligibleForOnboarding,\n            isOnboarded\n        }\n    }\n    subscriber {\n        subscriberStatus\n        subscriptionAtRisk\n        overlappingSubscription\n        doubleBilled\n        doubleBilledProviders\n        subscriptions {\n            id\n            groupId\n            state\n            partner\n            isEntitled\n            source {\n                sourceType\n                sourceProvider\n                sourceRef\n                subType\n            }\n            paymentProvider\n            product {\n                id\n                sku\n                offerId\n                promotionId\n                name\n                entitlements {\n                    id\n                    name\n                    desc\n                    partner\n                }\n                categoryCodes\n                redeemed {\n                    campaignCode\n                    redemptionCode\n                    voucherCode\n                }\n                bundle\n                bundleType\n                subscriptionPeriod\n                earlyAccess\n                trial {\n                    duration\n                }\n            }\n            term {\n                purchaseDate\n                startDate\n                expiryDate\n                nextRenewalDate\n                pausedDate\n                churnedDate\n                isFreeTrial\n            }\n            cancellation {\n                type\n                restartEligible\n            }\n            stacking {\n                status\n                overlappingSubscriptionProviders\n                previouslyStacked\n                previouslyStackedByProvider\n            }\n        }\n    }\n}\n\n    \nfragment account on Account {\n    id\n    attributes {\n        blocks {\n            expiry\n            reason\n        }\n        consentPreferences {\n            dataElements {\n                name\n                value\n            }\n            purposes {\n                consentDate\n                firstTransactionDate\n                id\n                lastTransactionCollectionPointId\n                lastTransactionCollectionPointVersion\n                lastTransactionDate\n                name\n                status\n                totalTransactionCount\n                version\n            }\n        }\n        dssIdentityCreatedAt\n        email\n        emailVerified\n        lastSecurityFlaggedAt\n        locations {\n            manual {\n                country\n            }\n            purchase {\n                country\n                source\n            }\n            registration {\n                geoIp {\n                    country\n                }\n            }\n        }\n        securityFlagged\n        tags\n        taxId\n        userVerified\n    }\n    parentalControls {\n        isProfileCreationProtected\n    }\n    flows {\n        star {\n            isOnboarded\n        }\n    }\n}\n\n    \nfragment profile on Profile {\n    id\n    name\n    isAge21Verified\n    attributes {\n        avatar {\n            id\n            userSelected\n        }\n        isDefault\n        kidsModeEnabled\n        languagePreferences {\n            appLanguage\n            playbackLanguage\n            preferAudioDescription\n            preferSDH\n            subtitleAppearance {\n                backgroundColor\n                backgroundOpacity\n                description\n                font\n                size\n                textColor\n            }\n            subtitleLanguage\n            subtitlesEnabled\n        }\n        groupWatch {\n            enabled\n        }\n        parentalControls {\n            kidProofExitEnabled\n            isPinProtected\n        }\n        playbackSettings {\n            autoplay\n            backgroundVideo\n            prefer133\n            preferImaxEnhancedVersion\n            previewAudioOnHome\n            previewVideoOnHome\n        }\n    }\n    maturityRating {\n        ...maturityRating\n    }\n    flows {\n        star {\n            eligibleForOnboarding\n            isOnboarded\n        }\n    }\n}\n\n\nfragment maturityRating on MaturityRating {\n    ratingSystem\n    ratingSystemValues\n    contentMaturityRating\n    maxRatingSystemValue\n    isMaxContentMaturityRating\n}\n\n\n',
        'operationName': 'login',
        'variables': {
            'input': {
                'email': f'{correo}',
                'password': f'{password}',
            },
        },
    }
    print(f"\n{r}[*]{b}Checkeando Disney Plus...\n")
    response_ds = requests.post(
        'https://disney.api.edge.bamgrid.com/v1/public/graphql', headers=headers_ds, json=json_data_ds)
    if "idp.error.identity.bad-credentials" in response_ds.text:
        print(f"{r}No tiene disney plus\n")
    elif response_ds.status_code != 200:
        print(f"{r}No se pudo checkear, Vuelva a intentarlo mas tarde\n")
    else:
        print(f"{v}Tiene disney plus\n")
####hbo max
    print(f"{r}[*]{m}Checkeando Hbo Max...\n")

    headers_hbo = {
        'Host': 'commerce-experience-latam.api.hbo.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': '*/*',
        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json; charset=utf-8',
        'X-B3-Traceid': '46a6c3b0-f01a-4a15-872f-53ad8f8f978b-hboMax-c406c83e-eb50-41f4-907a-3a6a7c96eb79',
        'X-Hbo-Client-Version': 'Commerce-Experience/1.6.82 desktop (DESKTOP)',
        'X-Hbo-Headwaiter': 'globalization:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImkiOiJnYXRld2F5QDAuMC4yODEiLCJ2IjoxLCJzIjo0Mn0.eyJkIjp7InVpTGFuZ3VhZ2UiOiJlcy00MTkiLCJmb3JtYXQiOiJlcy1DTyIsImFsdGVybmF0ZVVpTGFuZ3VhZ2UiOiJlcy00MTkiLCJwcmVmZXJyZWRMYW5ndWFnZXMiOlsiZXMtNDE5Il19LCJpYXQiOjE2NTYyNzc1NDV9.fam9GVfm4-hafc7SURmntuzDL-OosntXBjQx4F-eNIk,entitlements:eyJpIjoiZ2F0ZXdheUAwLjAuMjgxIiwidiI6MSwicyI6NDIsImFsZyI6ImRpciIsImVuYyI6IkEyNTZHQ00ifQ..KHlbqktDhUj9An39._upG4acnvgLPylBrMCyxWNQbUDSdtJALrI3D9t_wEatrnLUZKimnZ_BGdocjjgVhdRMg51VI9tBq5VW71iFvsK-sEFaPrLTFjFwL6-mNQDj409MqBnqkRjxuo22gvJFrpMHsro9iVrLM_TI_4sgMaelvIAEM1wiipCOClK8pT_r81IM2HsjvWsC7TTQas8-8HcHXlAQPCEQ1mCYuwswX_qSSupKiWzm0t7nKENuK5IxERfmUsXmNwGGx8tYb29KrrnHUF1BVVZ_zsQPkoGY21wJ1qjVufyPHZInvnD-qHotOBA0FocMP9DWYOeln7QrwPwyKWBV5Zqgrjgh38n5fjZ3ougSmWdg1CNUG7UbdA1SAvx-GVfqm-8tMzgzK5gVFsh95R0R80O514Bto4J_fHG8981FM8BcyFV_oJl5cxATbRqy6Xam__T9APoYDK1tbjfKcsNc.x1BcdvxcIaZuCU50kWJUnA,',
        'X-Recaptchaenttoken': 'HFZDc1d04TAlJWRzMASh0RS1BSPWtXEllxGFVwHm9FPU41K3RhESdVHU1YYHM8cgYNR1dmF1NGZlNFAzQ4QHIZM00gNkgcBWQ_IzkyOxgEThEcKXVgRz5TASARZhUbUBgAA1BsOFVDHndOBDIPRyInRDICSyURRwIReEMuJQwcVSUqBGRGAEMw',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aW1lc3RhbXAiOjE2NTYyNzc1NDUzNzQsImV4cGlyYXRpb24iOjE2NTYyOTE5NDUzNzQsInBheWxvYWQiOnsiaGlzdG9yaWNhbE1ldGFkYXRhIjp7Im9yaWdpbmFsSXNzdWVkVGltZXN0YW1wIjoxNjU2Mjc3NTQ1Mzc0LCJvcmlnaW5hbEdyYW50VHlwZSI6ImNsaWVudF9jcmVkZW50aWFscyIsIm9yaWdpbmFsVmVyc2lvbiI6Mn0sImV4cGlyYXRpb25NZXRhZGF0YSI6eyJhdXRoelRpbWVvdXRNcyI6MTQ0MDAwMDAsImF1dGhuVGltZW91dE1zIjozMTEwNDAwMDAwMCwiYXV0aHpFeHBpcmF0aW9uVXRjIjoxNjU2MjkxOTQ1Mzc0LCJhdXRobkV4cGlyYXRpb25VdGMiOjE2ODczODE1NDUzNzR9LCJ0b2tlblByb3BlcnR5RGF0YSI6eyJjbGllbnRJZCI6IjU0MjFhYjQ4LWVmNjktNDIzMS04ZGI0LWRiYTRmYWNjNjI5NyIsImRldmljZVNlcmlhbE51bWJlciI6IjUzNjhhMjllLTBmZDgtNDU1NS04ZTdhLTJmNGY5MWVkMzU4MCIsInBlcm1pc3Npb25zIjpbXSwiY291bnRyeUNvZGUiOiJVUyIsInBsYXRmb3JtVGVuYW50Q29kZSI6Imhib0RpcmVjdCIsInByb2R1Y3RDb2RlIjoiaGJvTWF4IiwiZGV2aWNlQ29kZSI6ImRlc2t0b3AiLCJwbGF0Zm9ybVR5cGUiOiJkZXNrdG9wIiwic2VydmljZUNvZGUiOiJIQk9fTUFYIiwiY2xpZW50RGV2aWNlRGF0YSI6e319LCJjdXJyZW50TWV0YWRhdGEiOnsiZW52aXJvbm1lbnQiOiJwcm9kdWN0aW9uIiwibWFya2V0IjoidXMiLCJ2ZXJzaW9uIjoyLCJub25jZSI6ImI3NTVkZWJjLTA1NTMtNGFlZC04MzIzLTRlN2FjNDhjYTY0ZCIsImlzc3VlZFRpbWVzdGFtcCI6MTY1NjI3NzU0NTM3NH0sInBlcm1pc3Npb25zIjpbXSwidG9rZW5fdHlwZSI6ImFjY2VzcyIsImVudmlyb25tZW50IjoicHJvZHVjdGlvbiIsIm1hcmtldCI6InVzIiwidmVyc2lvbiI6Mn19.EVsq7M9br_af3h8DuwVP1oU97OvI9etYjYIM7oWZk9k',
        'Origin': 'https://www.hbomax.com',
        # 'Content-Length': '96',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        # Requests doesn't support trailers
        # 'Te': 'trailers',
    }

    json_data_hbo = {
     'username': f'{correo}',
     'password': f'{password}',
     'clientFlow': 'buyflow',
    }

    response_hbo = requests.post('https://commerce-experience-latam.api.hbo.com/api/login', headers=headers_hbo, json=json_data_hbo)
    if response_hbo.status_code == 401:
        print(f"{r}No tiene Hbo Max\n")
    elif correo in response_hbo.text:
        print(f"{v}Tiene Hbo Max\n")
    elif response_hbo.status_code != 200 or 202 or 401:
        print(f"{r}No se ha podido comprobar, intente denuevo mas tarde...\n")


def opcion_inicial():
    print(banner)
    print(f"{r}[*]{w}1. Para ir al checker \n{r}[*]{w}2. Para Salir")
    opcion = int(input("Digite que quiere hacer: "))
    if opcion == 1:
        print(f"\n{v}Dirigiendose al checker...")
        sleep(3)
        checker()
    elif opcion == 2:
        print(f"{r}Saliendo...")
        sleep(3)
        exit()
    else:
        print(f"{r} Opcion incorrecta...")
        sleep(3)
        os.system("cls")
        print(banner)
        opcion_inicial()


opcion_inicial()
