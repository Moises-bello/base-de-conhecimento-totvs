---
article_id: 18949249527063
category: FÉRIAS
content_hash: 6c20a04c0b00418751a7e5dcb7f6090a501ab4a5ab3d15c678bce0a105e3a0f5
fetched_at: '2026-06-28T22:44:34.516288+00:00'
product: protheus
section_id: 10299705719575
source: central-protheus
title: RH - Linha Protheus - MEU RH - Para que serve o parâmetro MV_MRHS13F ?
type: support-article
updated_at: '2026-06-22T19:18:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18949249527063-RH-Linha-Protheus-MEU-RH-Para-que-serve-o-par%C3%A2metro-MV-MRHS13F
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18949239119895) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Para que serve o parâmetro **MV\_MRHS13F** ?   
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**O parâmetro tem a finalidade de **bloquear solicitações de férias com antecipação do 13° salário nos meses de Dezembro e Janeiro**.  
  
Abaixo os dados do novo parâmetro:

| Campo | Conteúdo |
| --- | --- |
| Nome da variável (X6\_VAR): | **MV\_MRHS13F** |
| Tipo (X6\_TIPO): | L - (Lógico) |
| Descrição (X6\_DESCRIC): | Permite solicitar a antecipação do 13 salario em |
| Descrição 1 (X6\_DESC1): | férias iniciadas nos meses de Dezembro e Janeiro. |
| Descrição 2 (X6\_DESC2): | .T. permite, .F. não permite, padrão .T. |
| Valor Padrão (X6\_CONTEUD): | .T. |

**Importante:**Por padrão, o Meu RH não exibe a solicitação de antecipação do 13º salário nas férias, caso as férias sejam iniciadas em Dezembro. Contudo, não havia bloqueio para o mês de Janeiro.  
  
Esse novo parâmetro visa travar principalmente o mês de Janeiro e proteger o Meu RH para solicitações realizadas no mês de dezembro por softwares externos ao Meu RH.  
  
O novo parâmetro estará disponível a partir da versão 12.1.2310, contudo, pode-se criá-lo manualmente, conforme a necessidade.  
  
**Saiba Mais  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
