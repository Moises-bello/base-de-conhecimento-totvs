---
article_id: 4936920098199
category: Evento S-2240
content_hash: 5936a4cbf385a639d9cfd5f6b5fc2d98c213c616a7dd015f9852b380da04af5c
fetched_at: '2026-06-28T22:45:23.568508+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Como funciona o envio das informações
  do S-2240. É necessário enviar apenas o que foi alterado após a carga inicial
type: support-article
updated_at: '2025-03-11T18:43:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4936920098199-RH-Linha-Protheus-MDT-eSocial-S-2240-Como-funciona-o-envio-das-informa%C3%A7%C3%B5es-do-S-2240-%C3%89-necess%C3%A1rio-enviar-apenas-o-que-foi-alterado-ap%C3%B3s-a-carga-inicial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25305469024151)**Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Como funciona o envio das informações do S-2240? É necessário enviar apenas o que foi alterado após a carga inicial? É possível retificar?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**O evento S-2240 exige uma carga inicial com data de início da condição igual à data de início da obrigatoriedade dos eventos de SST no eSocial. Após essa carga inicial, a alteração de qualquer das informações que compõe a estrutura do evento S-2240 exigirá o envio de um novo evento, descrevendo a situação atual, ou seja, descrevendo toda a exposição do trabalhador naquela nova data de início da condição e assim sucessivamente.  
  
**Exemplo:** Quando do início da obrigatoriedade do evento S-2240, em uma empresa do 1º grupo há um trabalhador exposto a 2 agentes nocivos com as seguintes datas de início de condição:

• calor (01/01/2020);

• ruído (01/06/2020).  
  
O eSocial somente registrará as informações de exposição a partir do início da obrigatoriedade dos eventos de SST. Assim, no exemplo e considerando a atual data de início da obrigatoriedade dos eventos de SST para o primeiro grupo (13.10.2021), deve ser feita a carga inicial do evento S-2240 até o dia 15.11.2021, registrando como data de início da condição o dia 13.10.2021 para os dois agentes nocivos, conforme dispõe a descrição do campo no leiaute “informar a data em que o trabalhador iniciou as atividades nas condições descritas ou a data de início da obrigatoriedade deste evento para o empregador no eSocial, a que for mais recente.  
  
Agora suponhamos que em 01.11.2021 o agente nocivo ruído deixou de existir e foi incluído o agente nocivo “radiações ionizantes”. Neste caso será enviado um novo S-2240 com essa data de início da condição informando os riscos “calor” e “radiações ionizantes”, excluindo o risco “ruído” e replicando as demais informações que não foram alteradas, como, por exemplo, o responsável pelos registros ambientais.  
  
Suponhamos, ainda, que no dia 13.03.2022 foi alterado o responsável pelos registros ambientais de “A” para “B”. Nesse caso, deverá ser encaminhado um novo evento S-2240, com data de início da condição em 13.03.2022, replicando as informações do evento anterior que não sofreram alterações e alterando apenas o responsável pelos registros ambientais.  
  
É importante destacar que as alterações acima, por consistirem em mudanças da informação anteriormente informada, não devem ser encaminhadas em eventos de retificação (que somente devem ser usados para corrigir informações equivocadas), mas sim encaminhadas em novo evento com nova data de início da condição.  
  
Fonte: [Perguntas frequentes](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes)  
  
**Saiba Mais**  
[Artigos sobre Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos sobre MDT eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
