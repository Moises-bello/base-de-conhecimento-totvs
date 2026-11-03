---
article_id: 360051779493
category: RH - Arquivos Magnéticos
content_hash: 252c0b866909d88c8ca6cc46b1e6fff3f5bb3912a7700b570510e01da49d8d0d
fetched_at: '2026-06-28T22:44:55.237870+00:00'
product: protheus
section_id: 32302371669783
source: central-protheus
title: RH - Linha Protheus - PON - ACJEF Código de Hora Extra utilizado em mais de
  um tipo
type: support-article
updated_at: '2025-09-11T13:31:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051779493-RH-Linha-Protheus-PON-ACJEF-C%C3%B3digo-de-Hora-Extra-utilizado-em-mais-de-um-tipo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34865363158295) Tempo aproximado para leitura: **00:01:00 min**  
Dúvida**O que verificar quando no módulo Ponto Eletrônico, ao gerar o  Arquivo de Controle de Jornada para Efeitos Fiscais (ACJEF), apresenta o log de ocorrência:  "Código de Hora Extra utilizado em mais de um tipo"?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
**Solução**Esta mensagem tem relação com a rotina Tipos de Horas Extras.  
  
O Sistema tem a premissa de termos cadastrado, os oito tipos de horas extras principais com eventos diferentes entre eles, não podemos repetir o mesmo evento em mais de um tipo de hora extra.  
  
Veja abaixo, exemplo de cadastro correto:

![](https://totvssuporte.zendesk.com/attachments/token/exmA5ykDCUyEQSRQSvCVmdFiD/?name=inline711195103.png)​

Note que tenho cadastrado todos os oito primeiros tipos de horas extras e, não repito nenhum evento em mais de um tipo.  
  
Deverão, para corrigir, analisar essa rotina e alterar os cadastros, inserindo novos eventos, para que cada tipo de hora extra tenha o seu específico.  
  
O ACJEF gera os eventos de Hora Extra, conforme estão gravados nas tabelas RFF e RFG, períodos abertos e fechados, respectivamente, com isso, ao gerar o ACJEF e tivermos Horas Extras a serem impressas, o Sistema irá validar o código gravado na tabela RFF ou RFG com o evento que está hoje, cadastrado na tabela SP4.  
  
Nesse caso, não orientamos a alteração dos códigos de eventos na rotina Tipos de Horas Extras, tabela SP4, pois se um dia o evento de Hora Extra normal foi apontado e calculado no código 100, por exemplo e, hoje na tabela SP4 foi alterado o evento autorizado de Hora Extra normal para 101, o ACJEF irá realizar uma comparação e, por estar divergente, o arquivo magnético não irá ser impresso.  
  
A solução seria, retornar o cadastro dos Tipos de Horas Extras, aos eventos que eram anteriormente, para geração do ACJEF, por isso, é importante ressaltar que, não orientamos, alterar os códigos de eventos autorizados na rotina Tipos de Horas Extras, se houver necessidade de mudança de contabilização de hora extra, alterar o cadastro do evento em si, preservando sempre o código dele na SP4, para não termos divergência com a RFF ou RFG.   
  
**Saiba mais:**  
[Boletim Técnico - AEJ](https://tdn.totvs.com/pages/releaseview.action?pageId=706906445)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
