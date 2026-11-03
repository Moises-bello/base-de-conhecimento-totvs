---
article_id: 360045693153
category: esocial - Periódicos
content_hash: 5cefc6e57674b0a398d113ed3ee91f22e6ebe79e2e83ca0ba54bff327971a771
fetched_at: '2026-06-28T22:47:09.262051+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 162 ao transmitir S-1299: Trabalhador consta
  na base do eSocial mas não foi informada sua remuneração'
type: support-article
updated_at: '2025-07-02T13:56:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045693153-RH-RM-FOP-eSocial-Erro-162-ao-transmitir-S-1299-Trabalhador-consta-na-base-do-eSocial-mas-n%C3%A3o-foi-informada-sua-remunera%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24510949953175) Tempo aproximado para leitura: 00:02:00 min  
  
Ocorrência**Ao realizar a transmissão do S-1299 referente ao período de apuração mensal para o governo é retornado a inconsistência **O Trabalhador com CPF : XXXXXXXXXXX e Matricula : XXXXXXXXXXXXXX consta na base de dados do Ambiente Nacional do eSocial, mas não foi informada sua remuneração. Ação Sugerida: Verificar se a falta de informação e decorrente de dificuldades operacionais ou se e possível efetuar a regularização.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28862492195223)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões   
  
 **Causa**Esta mensagem indica que existem funcionários que possuem vínculo empregatício com a empresa, porém não foram enviados os eventos de remuneração (S-1200) para o ambiente do eSocial.  
  
**Solução**  
 Para solucionar essa ocorrência, realize as seguintes validações:  
  
• **Dados Divergentes** enviados na Admissão  
Certifique-se que as categorias dos funcionários estão corretamente informadas no Portal do eSocial. Caso necessário ajuste da categoria, deve-se retificar o evento S-2200. No caso de troca de uma categoria **com** vínculo para uma **sem** vínculo empregatício, verifique a necessidade de exclusão do S-2200 com posterior envio do S-2300.

• **Falta** do registro de **Remuneração**Nos casos em que o Governo não localizar a remuneração do funcionário, será necessário verificar o motivo de não ter enviado o registros, as vezes, o eventos é rejeitado pelo RET e está na rotina Monitoramento do TAF. Nesse caso, identifique a inconsistência para corrigi-la e transmitir novamente ao eSocial.

• Funcionário **afastado**Para o funcionário afastado, deve conter no envelope de pagamento a verba de código de cálculo **315 - Base de FGTS de Afastados** para o envio no S-1200. O lançamento da verba para o envelope de pagamento é automático e realizado no momento do lançamento dos códigos de cálculos **1 - Horas Normais, 2 - Dias Trabalhados**ou **145 - Atestado Médico**, quando identificado que o funcionário possui o afastamento registrado no mês corrente.  
Depois, na [Geração dos Eventos Periódicos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003044711-RM-eSocial-Gera%C3%A7%C3%A3o-dos-eventos-peri%C3%B3dicos?source=search), selecione a situação dos funcionário que possuem a verba lançada no envelope de pagamento.  
  
**Saiba Mais**Para mais informações acesse:   
      • [Envio do evento S-1200 mensal para funcionários afastados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037949633-RM-eSocial-Envio-do-evento-S-1200-mensal-para-funcion%C3%A1rios-afastados?source=search)      • [Gerar XML Periódicos](https://tdn.totvs.com/pages/viewpage.action?pageId=452719232)
