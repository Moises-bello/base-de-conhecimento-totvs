---
article_id: 360025500013
category: Espelho
content_hash: 579e08304c87ae180cd153d8a2cab485599e57364bb01cbbd7b45ff4b4f1381a
fetched_at: '2026-06-28T22:46:31.308306+00:00'
product: rm
section_id: 6045459696023
source: central-rm
title: 'RH - RM - PTO - Horário: No espelho de ponto a jornada para um dia/data está
  errada'
type: support-article
updated_at: '2025-10-15T16:15:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025500013-RH-RM-PTO-Hor%C3%A1rio-No-espelho-de-ponto-a-jornada-para-um-dia-data-est%C3%A1-errada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19408759779735) Tempo aproximado para leitura: 00:01:30 min  
  
Ocorrência**  
Ao acessar o espelho do funcionário, a jornada esperada para um dia está errada.  
Exemplo: Domingo deveria ser descanso, está com definido como trabalho.  
  
**Ambiente**RH - RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80  
  
**Causa**Esse incidente é causado devido a associação dos índices das jornadas do horário, no momento associar o horário ao funcionário.  
  
**Solução**Veja que no espelho do funcionário, o mesmo está folgando nos dias de terça-feira e sexta-feira, sendo que o desejado neste caso seria sábado e domingo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30089599150103)  
  
Para corrigir, siga os passos abaixo:

1. Acesse na visão do espelho de ponto a opção **Processos | Alteração por Escala e Descanso** e edite os seguintes campos:  
   1-Código do horário: Informe o código do horário.  
   2-Mantém horário para funcionários: marque a flag  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30089621027095)
2. Confira no calendário a partir de qual dia o horário deve passar a valer para o funcionário. No exemplo quero começar a contar para a partir do sábado 01/02.  Depois clique em cima do nome do horário (descrição em azul) para ser aberto a tela do cadastro do horário.   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30089621028631)
3. Após abrir a tela de cadastro do horário, clique na aba jornada, e confira qual o índice se refere a jornada de compensado, no meu caso é o índice 6.    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30089599157399)
4. No campo **Índice da data de mudança** informe o índice referente ao dia de compensado que no exemplo é o 6, (o Índice da data base será preenchido automaticamente).  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30089621036311)
5. Aqui como o dia/data da mudança é um sábado, irei clicar no **campo/célula** abaixo do **dia/data**, para que ele fique selecionado e logo após clico no botão **Aplicar na Seleção**.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30089599162007)  
     
   No meu caso, como eu já havia feito a vinculação de horário para este o dia o campo não está        vazio, ele está preenchido como H.1, indicando que houve essa alteração no período ativo. Assim ao clicar no botão aplicar na seleção vai aparecer a mensagem abaixo:  
     
   *Você confirma a remoção dos horários(s) e/ou descanso(s) selecionado(s)?**Isso poderá implicar na remoção dos registros no histórico de horários do funcionário.*Clique no botão **ok**.  
   *![](https://centraldeatendimento.totvs.com/hc/article_attachments/30089599163159)*Após clicar em ok, no campo/célula abaixo da data vai estar preenchido com o código do      horário.

    Observação: Caso no seu dia/data o campo esteja vazio, logo após em clicar no botão Aplicar na          Seleção, o campo/célula vai ser preenchido com o código do horário.    
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30089599168791)

6. Caso queira visualizar se associação do horário ficou correta antes de concluir o processo, clique no botão **Visualizar Horário Planejado**. E por aqui já podemos confirmar que as jornadas de compensado e descanso do horário caíram nos dias certos.    
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30089621043735)

    7. Feche a tela de visualização do horário, avance e execute o processo.    
    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30089621046679)  
  
   8. Ao voltar na visão do espelho de ponto os dias de descanso e compensado já estarão atualizados.     
    [![](https://centraldeatendimento.totvs.com/hc/article_attachments/30089599177879)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021943091)  
  
**Saiba mais:**[RH - RM - PTO - Associar/alterar de forma global o horário por intervalo dos funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000289207)  
[RH - RM - PTO - Alteração de Horário - escolha do índice pelo campo data base](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011812211)
