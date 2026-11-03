---
article_id: 360043106933
category: Escrita Fiscal - Error.log
content_hash: 5a1617593f36452595228b2346d0f66a6b0a40dc822c95497106214208368cc9
fetched_at: '2026-06-28T22:39:32.812002+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como fazer preenchimento
  do campo FT_CONTA
type: support-article
updated_at: '2021-07-08T13:49:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043106933-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-fazer-preenchimento-do-campo-FT-CONTA
---

**Ocorrência**Como preencher o campo FT\_CONTA no Protheus?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 12  
  
**Solução**

Para preenchimento do campo FT\_CONTA é necessário que o TES esteja configurado para gerar Livros, **(F4\_LFIPI / F4\_LFICM  diferente de NÂO),**o preenchimento da conta contábil no cadastro de produtos trará automaticamente a conta no lançamento do pedido ou poderá preencher manualmente uma conta valida.   
  
**Segue exemplos:**  
**![](https://totvssuporte.zendesk.com/attachments/token/F94Zuu0nw1E4Jtjwp5FeSHNG5/?name=inline-1584288494.png)​**  
  
  
**![](https://totvssuporte.zendesk.com/attachments/token/afLqprkxCitHJxAWoHY1feddP/?name=inline2076897514.png)​**  
  
**![](https://totvssuporte.zendesk.com/attachments/token/5Ry1TshGc9QFOC6bPVtbVafiO/?name=inline308257439.png)​**  
  
  
  
**![](https://totvssuporte.zendesk.com/attachments/token/jzKoWQex8nywWYZ7E7WWDljpD/?name=inline162309185.png)​**  
**Relacionado**  
\*\* Quanto ao rateio :=   
*Para todos os registros do bloco A, C, e D que são oriundos de documentos fiscais, o sistema realiza o procedimento abaixo:*  
As informações deste campo têm origem da tabela do cadastro de Plano de Contas (CT1). Este registro é gerado com a Conta Contábil informada na nota fiscal.  
  
Para o preenchimento automático dos campos D1\_CONTA e C6\_CONTA é necessário utilizar o campo CTA CONTABIL(B1\_CONTA) na cadastro de Produtos (SB1). Ao escriturar o documento fiscal, o número da Conta Contábil Será gravadas na Tabela SD2 no campo D2\_CONTA para Nota fiscal de Saída e na Tabela SD1 no campo D1\_CONTA para documentos de entrada. Na TABELA de Item do Livros FISCAL SFT no campo FT\_CONTA.  
  
Uma vez que não preencher o campo B1\_CONTA, deve ser Preenchido no momento da Inclusão do Pedido/Documento  
Pedido de Vendas - C6\_CONTA  
Documento de Entrada - D1\_CONTA  
Lembrando que o fonte do Geração do Arquivo EFD Contribuições(FISA008) consideras as informações gravadas no Livros Fiscais e dessa forma será considerado a Conta Contábil gravada no campo **FT\_CONTA** referente ao produto amarrado a NF.  
  
**Atenção:**  
Para os casos de operações que possuem rateio (duas ou mais contas contábeis) ou quando algum dos campos acima não possam ser preenchidos, será necessário utilizar o ponto de entrada SPDPIS07 para gravação correta da conta contábil nos registros acima e no registro 0500:  
Informações sobre o ponto de entrada SPDPIS07: <http://tdn.totvs.com/display/public/PROT/SPDPIS07+-+Registro+0500>
