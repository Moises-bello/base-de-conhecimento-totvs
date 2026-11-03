---
article_id: 41185757581335
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 8897e18da4005150b94a8439eda451bee02ad12219f82c883036aec009f5bb92
fetched_at: '2026-06-28T22:37:24.180717+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Uso de Rateio na Medição
  limpa o campo CNE_CONTA - Conflito com o SPED Contribuições
type: support-article
updated_at: '2026-06-12T20:26:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41185757581335-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Uso-de-Rateio-na-Medi%C3%A7%C3%A3o-limpa-o-campo-CNE-CONTA-Conflito-com-o-SPED-Contribui%C3%A7%C3%B5es
---

Ao usar rateio na medição de contratos, o sistema limpa automaticamente a conta contábil no campo "CNE\_CONTA", onde ao gerar o Pedido, a informação fica apenas na tabela SDE, o que causa erro no SPED Contribuições. A conta contábil pode ser informada manualmente na NF de entrada (campo D1\_CONTA) ou, para preenchimento automático na Medição, é possível criar uma customização via pontos de entrada da rotina.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41185789742615) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Ao realizar uma medição de um contrato e no Rateio é informada a conta contábil no campo “CNZ\_CONTA” o sistema automaticamente limpa a conta do campo “CNE\_CONTA”. Com essa situação quando é gerado o pedido de compras e posteriormente o Documento de entrada a conta contábil fica apenas na tabela SDE de rateio e dessa forma a informação da conta não é gerada na tabela SFT no campo “FT\_CONTA” e isso ao gerar o SPED Contribuições apresenta erro de falta de conta contábil. Como podemos proceder nessa situação?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Por padrão do módulo ao se utilizar o Rateio na rotina de medição a rotina por padrão tem a funcionalidade de limpar o campo de entidades contábeis informadas o item da planilha da medição.  
   
Este se trata de fato da forma como a rotina padra trabalha conforme seu conceito.  
   
   
Para o SPED Contribuições a informação da conta contábil (D1\_CONTA) pode ser informada manualmente no momento da inclusão da NF de entrada no campo D1\_CONTA conforme a necessidade.  
   
   
E no caso da rotina de medição para um preenchimento automático do pedido de compras gerado na medição caso deseje pode-se realizar através de uma customização conforme a necessidade.  
Enviamos abaixo artigo com os pontos de entrada disponíveis da rotina para que possa avaliar algum que melhor possa atender conforme a necessidade.  
   
Sugestão de PE:  
[DT\_PE\_CN121PED\_Tratamento\_especifico\_antes\_da\_geração\_do\_pedido\_de\_compra](https://tdn.totvs.com/pages/viewpage.action?pageId=271385565)  
   
Demais PE da rotina:  
[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pontos de entrada para rotina de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Pontos-de-entrada-para-rotina-de-Medi%C3%A7%C3%A3o)  
   
   
   
Sobre este padrão do sistema, caso deseje, para uma forma diferente de seu funcionamento, o que podemos orientar é a abertura de uma sugestão de melhoria através da Central Colaborativa diretamente no Portal do Cliente conforme as informações mais abaixo.  
Este é o contato direto do cliente com a Equipe responsável pelo Produto.

***Saiba Mais:***

* [Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal e EFD Contribuições - Preenchimento da Conta Contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015964612-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-e-EFD-Contribui%C3%A7%C3%B5es-Preenchimento-da-Conta-Cont%C3%A1bil)
* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
