---
article_id: 9292790424471
category: Materiais - Compras (SIGACOM)
content_hash: 08142039437349db29b6cf33a1ac8ab87b296bd00721233db9c001301980ea37
fetched_at: '2026-06-28T22:41:14.151313+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao importar o XML é
  gerado o código de erro COM052 no reprocessar do Importador XML
type: support-article
updated_at: '2024-05-17T17:35:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9292790424471-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-importar-o-XML-%C3%A9-gerado-o-c%C3%B3digo-de-erro-COM052-no-reprocessar-do-Importador-XML
---

**Dúvida**

Ao realizar o processo de importação de um XML pelo Importador XML / TOTVS Colaboração ocorre o erro COM052.   
  
**Ambiente**Microsiga Protheus – Compras – A partir da versão 12.1.17  
  
**Solução**

Esse incidente normalmente ocorre, pois no arquivo **sigamat.emp (SYS\_COMPANY)** não existe o CNPJ que pertence a Empresa/Filial para este XML.

Para solucionar essa ocorrência, realize os seguintes passos:

**1.** Entre no Arquivo XML e verifique qual é o "TOMA" como demonstra no print abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23562445107991)

Toma 03= CNPJ do destinatário  
Toma 00= CNPJ do remetente  
Toma 01= CNPJ do expedidor  
Toma 02= CNPJ do recebedor  
Toma 04= CNPJ do própria tag no XML

Caso seja CTE temos a documentação a seguir: [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Inclusão de CTE via Importador XML – Central de Atendimento TOTVS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4427846804503-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Inclus%C3%A3o-de-CTE-via-Importador-XML)

Obs.: Quando não é tipo CTE, não existe tomador, pois o CNPJ precisa ser do destinatário.

**2.** Acesse o arquivo **sigamat.emp (SYS\_COMPANY)** e valide se o CNPJ se encontra cadastrado.  
**3.** Acesse a rotina Monitor(COMXCOL) através do caminho Miscelanea - Totvs Colaboração/Importador XML; Selecione a opção Reprocessar;  
**4.** Marque o documento com erro;  
**5.** Marque para qual filial deseja importar o documento e confirme.

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Inclusão de CTE via Importador XML – Central de Atendimento TOTVS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4427846804503-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Inclus%C3%A3o-de-CTE-via-Importador-XML)

[IX06 - Erros (Códigos) - Linha Microsiga Protheus - TDN (totvs.com)](https://tdn.totvs.com/pages/releaseview.action?pageId=485869227)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
