---
article_id: 40672834719895
category: SIGAEST - PODER DE TERCEIROS
content_hash: b26dba3a5e219434cacb15a244ec65a6f2e0b9d2426ef738ca852e2898b29c49
fetched_at: '2026-06-28T22:39:03.273239+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -Como agendar a rotina
  Refaz Poder de Terceiro (MATA216) via Schedule
type: support-article
updated_at: '2026-05-22T19:52:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40672834719895-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-agendar-a-rotina-Refaz-Poder-de-Terceiro-MATA216-via-Schedule
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40672834714135) Tempo aproximado para leitura: 00**:**01:00 **min**  
  
**Dúvida**  
Como realizar a configuração e o agendamento de forma nativa da rotina Refaz Poder de Terceiro (MATA216) por meio do Schedule no Protheus?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
Esta implementação tem como finalidade disponibilizar de forma nativa o processamento da rotina **Refaz Poder de Terceiro (MATA216)** por Schedule, sem a necessidade de criação de rdmakes para o acionamento automático do processamento.

A implementação não descontinua a possibilidade de execução da rotina em batch.

**Importante:** A funcionalidade está disponível na rotina MATA216 com a versão igual ou superior a 04/04/2024.

Essa rotina pode ser executada com o sistema em uso por todos os usuários. Nesse caso, as movimentações de terceiro que estão acontecendo simultaneamente ao cálculo podem influir no resultado. Para que a rotina seja executada dessa forma, o parâmetro **MV\_CUSTEXC** deve estar com o conteúdo igual a "**N**".

Outra forma de execução é com o sistema em modo exclusivo, sem outros usuários utilizando os arquivos necessários ao cálculo. Para que a rotina seja executada dessa forma, o parâmetro **MV\_CUSTEXC** deve estar com o conteúdo igual a "**S**", porém essa configuração interfere se o cliente utiliza a Thread do Agent do Schedule ou até mesmo se o configurador ficar aberto, dessa forma o recomendado é a utilização com "**N**".

Caso o parâmetro esteja como **"S"**e não seja possível obter acesso exclusivo para o processamento, a rotina não será executada.

**Passos**

* **Configuração de Schedule:**

Exemplo do cadastro do agendamento:

![](https://tdn.totvs.com/download/attachments/836511092/schedule_mata216.gif?version=1&modificationDate=1712258520677&api=v2)

* 2. Ánalise de Resultado:

Consultando os eventos através do botão "Visualizar" da rotina Refaz Poder de Terceiro, é possível visualizar se a rotina foi executada com sucesso.

![](https://tdn.totvs.com/download/attachments/836511092/consulta_mata216.gif?version=1&modificationDate=1712260633997&api=v2)

**No campo "Filial" deverá ser selecionada todas as filiais em que o processamento da rotina deverá ocorrer.**

Saiba mais:

[*Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538881-SIGAEST-PODER-DE-TERCEIROS)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA216: Qual o conceito e a usabilidade da rotina "Refaz Poder de/em Terceiros"?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35056725584023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA216-Qual-o-conceito-e-a-usabilidade-da-rotina-Refaz-Poder-de-em-Terceiros)

[Schedule MATA216 Refaz Poder de terceiro](https://tdn.totvs.com/display/public/PROT/Schedule+-+MATA216+-+Refaz+Poder+de+Terceiro+-+P12#Par%C3%A2metros-1)
