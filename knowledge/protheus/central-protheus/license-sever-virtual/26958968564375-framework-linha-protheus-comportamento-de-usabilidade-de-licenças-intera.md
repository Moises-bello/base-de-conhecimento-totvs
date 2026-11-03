---
article_id: 26958968564375
category: License Sever Virtual
content_hash: e88dc58bd22f4325486c19681bde1d5b98c0e58c17b9e2c6bf6e55406e49ba3b
fetched_at: '2026-06-28T22:42:20.027879+00:00'
product: protheus
section_id: 360000075428
source: central-protheus
title: Framework - Linha Protheus - Comportamento de usabilidade de licenças Intera.
type: support-article
updated_at: '2025-03-12T18:57:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26958968564375-Framework-Linha-Protheus-Comportamento-de-usabilidade-de-licen%C3%A7as-Intera
---

**Duvida?**  
Qual é o conceito do uso dos CNPJs no contrato Intera Ilimitado com o License Server?

**Ambiente**

Protheus – Servidor de Licenças - Todas as versões

**Solução:**

Na modalidade Intera Ilimitado, é necessário que todos os CNPJs utilizados sejam devidamente reportados à TOTVS.  
O License Server, como provedor de licenciamento dos produtos da TOTVS, é responsável por receber e armazenar os CNPJs reportados pelos ERPs vinculados à aplicação.  
Assim, é importante verificar quais CNPJs estão atribuídos às empresas e filiais cadastradas no seu ERP e realizar as devidas manutenções:

* Como avaliar os CNPJs cadastrados no Protheus;
* Como incluir
* Como excluir

1. Acesse o Configurador(Sigacfg)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26958955245847)

2. Menu Ambiente > Empresas > Filial

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26958968540951)

3. Selecione a Filial desejada e clique sobre ela;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26958968542359)

4. Clique em alterar e verifique o campo CNPJ;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26958968544023)

* **Os principais comportamentos a serem analisados nesse contexto incluem:**

* **Ambiente de teste com CNPJs diferentes do registrado para uso -** No ambiente de teste, analise os CNPJs cadastrados no registro das empresas.

* **Uso de dois contratos com modalidades diferentes (Tradional e Intera) -**  Avalie a utilização de Instalações TOTVS ID estão de acordo com os contratos e os devidos apontamentos dos ambientes (ERP's) para os seus *Licenseserver*, conforme seus contratos. Está configuração poderá ser avaliada conforme o ERP no License Server.
* **Protheus:**
* 1 - Na configuração do AppServer, verifique na seção *Licenseclient* o endereço do servidor e a porta configurada para o *Licenseserver*.

* **License Server Virtual:**
* 1 - Acesse o Monitor do *Licenseserver* correspondente.
* 2 - No menu de informações (ícone localizado no canto superior direito da tela), confirme o *TotvsId*.
* 3 - Entre no Portal do Cliente e acesse a empresa vinculada ao contrato.
