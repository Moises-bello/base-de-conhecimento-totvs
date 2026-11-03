---
article_id: 360038464054
category: RH - Rescisão
content_hash: 7c57422d2c35aba681994d5333c07d3b5e558ee262a69d740372c2e790c94d92
fetched_at: '2026-06-28T22:43:51.109433+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Cadastro de Aviso Prévio - (Aviso trabalhado)
type: support-article
updated_at: '2025-06-16T17:53:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038464054-RH-Linha-Protheus-GPE-Cadastro-de-Aviso-Pr%C3%A9vio-Aviso-trabalhado
---

**Dúvida**  
Cadastro de Aviso Prévio - (Aviso trabalhado) Rotina GPEA925.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Foi disponibilizado o Cadastro do Aviso Prévio (GPEA925) para utilização na transmissão do eSocial, que deve ser utilizado para registrar o evento S-2250 (Aviso Prévio).

Os dados aqui informados são referentes ao**layout 2.04.02** do eSocial, sempre deve ser observado o layout corrente para veracidade das informações.

O Cadastro será integrado com a Rescisão, trazendo na tela de rescisão os dados de Data de Aviso Prévio, dias de Aviso e Data de desligamento.

* **Tipo de Rescisão - Tipo Resc. (RFY\_TPRESC):**Selecionar o Tipo da Rescisão, conforme a tabela S043 - Tipos de Rescisão
* **Tipo de Aviso - Tp.Av.Prev. (RFY\_TPAVIS):** Informar o Tipo Aviso Prévio, sendo as opções  
  1 - Aviso prévio trabalhado dado pelo empregador ao empregado, que optou pela redução de duas horas diárias [caput do art. 488 da CLT];  
  2 - Aviso prévio trabalhado dado pelo empregador ao empregado, que optou pela redução de dias corridos [parágrafo único do art. 488 da CLT];  
  3-Aviso prévio dado pelo empregado (pedido de demissão), dispensado de seu cumprimento **(DESCONTINUADO NO ESOCIAL)**.   
  4 - Aviso prévio dado pelo empregado (pedido de demissão), não dispensado de seu cumprimento, sob pena de desconto, pelo empregador, dos salários correspondentes ao prazo respectivo (§2º do art. 487 da CLT);  
  5 - Aviso prévio trabalhado dado pelo empregador rural ao empregado, com redução de um dia por semana ( art. 15 da Lei nº 5889/73);  
  6 - Aviso prévio trabalhado decorrente de acordo entre empregado e empregador (art. 484-A, "caput", da CLT).  
    
  Portanto, não cabe o cadastramento do aviso quando o mesmo for **INDENIZADO.**  
    
  Com base nestas informações o cliente deverá preencher o GPEA925- cadastro de aviso prévio de acordo com a regra acima e conforme o seu cenário.  
  Lembrando que a informação do GPEA925 deverá condizer com a tabela S043:  
    
  ![](https://totvssuporte.zendesk.com/attachments/token/0WQF4GdDpsD9GBh2esuK4qyma/?name=inline1335274951.png)

**OBS:****A opção Aviso prévio Indenizado (dispensa pelo empregador) não foi disponibilizado, pois o envio dessa informação não é obrigatória segundo o layout do e-social disponibilizado pelo governo.**
