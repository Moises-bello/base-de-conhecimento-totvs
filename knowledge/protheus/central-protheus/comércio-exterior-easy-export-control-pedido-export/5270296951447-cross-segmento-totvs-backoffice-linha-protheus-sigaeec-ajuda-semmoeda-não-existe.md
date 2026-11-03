---
article_id: 5270296951447
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: 5e343ad12da8bcf961086faa572da0163fd3c49548fab70dfe58e4f2492b6a29
fetched_at: '2026-06-28T22:36:58.979257+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Ajuda: SEMMOEDA
  - Não Existe Moeda Cadastrada'
type: support-article
updated_at: '2022-04-06T14:52:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5270296951447-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Ajuda-SEMMOEDA-N%C3%A3o-Existe-Moeda-Cadastrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Ao tentar gravar o RA na rotina de pedido de exportação (EECAP100) apresenta o erro abaixo e não permite a geração do mesmo no contas a receber. Como faço para que este não seja exibida esta mensagem?

```
AJUDA:SEMMOEDA  
Não existe moeda cadastrada!

Tabela SE1 04/04/2022 17:01:29
No. Titulo           - E1_NUM       := 000000005
Prefixo              - E1_PREFIXO   := EEC
Parcela              - E1_PARCELA   :=  
Tipo                 - E1_TIPO      := RA
Cliente              - E1_CLIENTE   := EXP001
Loja                 - E1_LOJA      := 0001
DT Emissao           - E1_EMISSAO   := 30/03/2022
Vencimento           - E1_VENCTO    := 30/03/2022
Vencto real          - E1_VENCREA   := 30/03/2022
Vencto Orig          - E1_VENCORI   := 30/03/2022
Vlr.Titulo           - E1_VALOR     := 5551.4
DT Contab.           - E1_EMIS1     := 30/03/2022
Taxa moeda           - E1_TXMOEDA   := 4.75
Vlr R$               - E1_VLCRUZ    := 26369.15
Moeda                - E1_MOEDA     := 0 < -- Invalido
                     - CBCOAUTO     := 001
                     - CAGEAUTO     := 0695 
                     - CCTAAUTO     := 59424     
Natureza             - E1_NATUREZ   := 1001001   
Historico            - E1_HIST      := Ped.: EX1075              
Origem               - E1_ORIGEM    := sigaeec
--------------------------------------------------------------------------------
AJUDA:FALHATUDOK
Falha na execução dos processos de validaçao da rotina de geraçao de títulos (FINA040)
Erro na contratação.
```

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
**Solução**Será necessário efetuarem o seguintes procedimentos:  
1) Qual moeda esta sendo utilizada no processo .   
Exemplo: Caso seja dólar (**US$**) acesse o cadastro de moedas (**EECAT135**) e veja se o campo moeda ERP (**YF\_MOEFAT**) está com o valor 0 (o correto seria 2).  
  
2) Verifique como estão os conteúdos dos parâmetros **MV\_MOEDA,MV\_MOEDAP** e **MVSIMB**  e se existe algum nome parâmetro que esteja com a numeração 0 (não é para existir).   
Exemplo **MV\_MOEDA0, MV\_SIMB0**,etc.  
  
3) Acessar a rotina dos eventos contábeis (**ECOA002**), filtrar pelo módulo exportação, código **605 -ADTO DE CLIENTE** e verificar como esta o campo Tp. Título (**EC6\_TPTIT**).  O Conteúdo deste campo tem que estar como RA conforme imagem abaixo:

![EC6_TPTIT.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/5269630559639/EC6_TPTIT.PNG)

4) Verificar se os **avlinks** que são responsáveis pela integração com financeiro estão atualizados. Estes arquivos ficam disponíveis na pasta **\Protheus\_data\Comex\Easylink\** .Para efetuar o download dos pacotes disponíveis é necessário acessar o site da expedição continua do Comex.   
  
**Saiba mais**  
[Expedição continua Comex](https://tdn.totvs.com/pages/releaseview.action?pageId=526987588)
