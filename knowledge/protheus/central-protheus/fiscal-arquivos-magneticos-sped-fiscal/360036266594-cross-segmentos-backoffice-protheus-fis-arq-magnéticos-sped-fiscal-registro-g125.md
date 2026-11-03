---
article_id: 360036266594
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 7a8fc2d2de77ed0a596c61da3a55fc1292806e48c5675f3f6353fa18188c4d95
fetched_at: '2026-06-28T22:42:02.435807+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Sped Fiscal
  - Registro G125 duplicado
type: support-article
updated_at: '2025-03-19T17:51:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036266594-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Registro-G125-duplicado
---

**Ocorrência**O campo 05\_ VL\_IMOB\_ICMS\_OP está sendo gerado com valor duplicado.  
   
 **Ambiente**  
Microsiga Protheus – Livros fiscais – A partir da versão 11.80  
   
 **Causa**Este problema ocorre pois o parâmetro **MV\_F9VLLEG** está preenchido.  
   
 **Solução**Para os valores não serem gerados duplicados no registro G125, o parametro **MV\_F9VLLEG** deve estar em BRANCO (padrão do sistema).

Nome da Variável = **MV\_F9VLLEG**   
Tipo = Caracter  
Conteúdo = <branco>    
Descrição = Campo da tabela SF9 que indica o valor CIAP já apropriado no sistema   
Legado. O valor que completa o lançado no F9\_VALICMS quando utiliza o QTDPARC  
   
   
**Importante**   
Utiliza-se este tratamento quando não é informado o valor apropriado no sistema legado. Este valor é utilizado para compor o total de Crédito CIAP. Ex.: Ao incluir o CIAP, o campo Valor ICMS (F9\_VALICMS) é R$300,00 o QTDPARC é 30 e o SLDPARC é 30, portanto o Crédito CIAP para as 30 parcelas restante é +/- R$10,00, porém NÃO se tem o valor total do CIAP, o que se refere às 18 parcelas já apropriadas no outro sistema. Este campo a informar no parâmetro MV\_F9VLLEG deve representar o restante, que neste é R$180,00 dando um total de credito de R$ 480,00 em 48 parcelas.
