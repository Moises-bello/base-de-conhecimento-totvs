---
article_id: 360029356611
category: RH - Folha de Pagamento
content_hash: a7fd2f4ce847394b8a5f3a91dabebb53dbe0b78f1fd5d9602d028618cfa33a1b
fetched_at: '2026-06-28T22:44:11.931469+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE -  Separação de remuneração de funcionários afastados
  (Criação Ids de cálculo 1432 e 1433)
type: support-article
updated_at: '2026-01-08T12:55:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029356611-RH-Linha-Protheus-GPE-Separa%C3%A7%C3%A3o-de-remunera%C3%A7%C3%A3o-de-funcion%C3%A1rios-afastados-Cria%C3%A7%C3%A3o-Ids-de-c%C3%A1lculo-1432-e-1433
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26278493133719) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**  
Separação de remuneração de funcionários afastados (Criação Ids de cálculo 1432 e 1433)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Sistema não possui identificadores de cálculo para a geração das rubricas **9932** (Valor do benefício previdenciário pago por Previdência Social Oficial em função de afastamento por motivo de acidente de trabalho, para fins de apuração da base de cálculo do FGTS) e **9905**(Valor não relativo a vencimento ou desconto, relativo à remuneração a que teria direito, se em atividade, o trabalhador afastado do trabalho para prestação do serviço militar obrigatório.

Ajuste para efetuar a criação de novos identificadores de cálculo para o eSocial:  
  
- Id de cálculo **1432 - Valor de afastamento por acidente pago pela Previdência**: verba de base contendo a remuneração dos dias do afastamento por acidente de trabalho pago pela previdência. **Deve ter incidencia 12 para FGTS**  
  
- Id de cálculo **1433 - Valor de remuneração a que teria direito (Serviço Militar)**: verba de base contendo a remuneração que o funcionário afastado por licença militar teria direito.  
  
Após o ajuste, a verba de Id **1420 - Valor de afastamento por doença pago pela Previdência**irá conter a remuneração dos dias do afastamento por doença pagos pela previdência.  
  
**Importante**  
As verbas cadastradas para esse ID devem ser de base e não devem possuir incidências, pois são verbas de referência que não alteram o pagamento do funcionário.

**Saiba mais:**

[**RH - Folha de Pagamento**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
