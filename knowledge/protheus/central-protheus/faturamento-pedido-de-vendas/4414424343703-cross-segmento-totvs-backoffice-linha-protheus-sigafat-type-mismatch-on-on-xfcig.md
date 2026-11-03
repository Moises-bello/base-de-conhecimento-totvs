---
article_id: 4414424343703
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: ce407ec702eef84855131794f1c7116005aa9e1c9f54b7cba2d4c4fb5ef5174b
fetched_at: '2026-06-28T22:38:38.616878+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - type mismatch
  on $  on XFCIGETORIGEM(FCIXFUN.PRW)
type: support-article
updated_at: '2021-11-30T11:38:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414424343703-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-type-mismatch-on-on-XFCIGETORIGEM-FCIXFUN-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao incluir um pedido de devolução, o sistema gera o erro:

**type mismatch on $  on XFCIGETORIGEM(FCIXFUN.PRW) 15/09/2020 13:41:10 line : 378**

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Todas as versões  
  
**Causa**O erro informa que existe um tipo incompatível entre as variáveis **cEstado** e **cUfNwPrd**, cEstado recebe a informação do parâmetro **mv\_estado** e cUfNwPrd recebe a informação do parâmetro **MV\_FCINWPR**.  
  
Conforme a stack do erro, cEstado está recebendo um valor lógico e não o valor atribuído no **mv\_estado**, gerando incompatibilidade, necessário verificar se o parâmetro está cadastrado corretamente:  
  
STACK XFCIGETORIGEM(FCIXFUN.PRW) 15/09/2020 13:41:10  
  
  Param 1: CCODPROD(C) : N87169090-302   
  Param 2: DDTEMISSAO(D) : 2021/11/25  
  Local 1: CCODPROD(C) :N87169090-302   
  Local 2: DDTEMISSAO(D) :2021/11/25  
  Local 3: CPERIOD(C) :112021  
  Local 4: CORIGEM(C) :  
  Local 5: CFCICOD(C) :  
**Local 6: CESTADO(L) :.F.---->valor lógico .F. --variável recebe conteúdo do mv\_estado que não é do tipo lógico.**  
**Local 7: CUFNWPRD(C) :SP---> recebendo o estado**  
  Local 8: NCONT(N) :0  
  Local 9: DDATACALC(D) :00/00/00  
  Local 10: CFILIALCFD(C) :06  
  
  
**Solução**  
Para solucionar essa ocorrência, certifique-se que os parâmetros estejam configurados conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414431254807/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414424119319/mceclip1.png)

Caso não estejam, exclua e inclua novamente com esta configuração ou baixe o dicionário de dados e rode o upddistr para que o ajuste seja efetuado.

O **mv\_estado** e o **mv\_fcinwpr** precisam ser do mesmo tipo caráter para que comparação possa passar e não gerar conflitos.
