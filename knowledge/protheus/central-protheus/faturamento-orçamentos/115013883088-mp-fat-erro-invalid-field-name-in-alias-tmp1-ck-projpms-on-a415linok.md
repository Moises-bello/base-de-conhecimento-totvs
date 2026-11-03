---
article_id: 115013883088
category: Faturamento - Orçamentos
content_hash: 4613e3bb8d414849e26047acb67c3a6a9311d3cdb9edce05a7721af3f728bc3e
fetched_at: '2026-06-28T22:38:25.000230+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: MP-FAT-Erro invalid field name in Alias TMP1->CK_PROJPMS on A415LINOK
type: support-article
updated_at: '2021-04-28T15:15:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115013883088-MP-FAT-Erro-invalid-field-name-in-Alias-TMP1-CK-PROJPMS-on-A415LINOK
---

**Ocorrência**   
  
Erro na tela de orçamento: invalid field name in Alias TMP1->CK\_PROJPMS on A415LINOK(MATA415.PRX)  
  
**Causa**  
  
O erro ocorre quando há integração com o projeto do módulo PMS, onde há necessidade de informar o campo CK\_PROJPMS, pode ser que o campo não exista no ambiente ou não esteja em uso .  
  
**Ambiente**  
  
Microsiga Protheus - versão 11 e versão 12  
  
**Solução**  
   
Avalie se o campo CK\_PROJPMS está como usado no dicionário de dados, via configurador, pois o erro somente ocorre se o mesmo estiver com o uso desmarcado.  
Para ajustar:  
1-Edite a tabela SCK;  
2-Edite o campo CK\_PROJPMS;  
3-Marque-o como usado;  
4-Salve a tabela;  
5-Atualize o dicionário de dados;  
6-Reinicie o sistema e refaça o processo,  o erro deixará de ocorrer.

Obs: Tivemos clientes que apresentou o mesmo problema com os campos CK\_EDTPMS e CK\_TASKPMS, neste caso, faça o mesmo processo utilizado para o campo CK\_PROJPMS, que o erro deixará de ocorrer.

Outro impeditivo é se o nível desses campos (CK\_PROJPMS, CK\_EDTPMS e CK\_TASKPMS) forem alterados, também ocorre o erro, por padrão mantenha como nível 1.
