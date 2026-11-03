---
article_id: 26355201093271
category: Espelho
content_hash: 18783f4a6c777389228344af7b0d596a424a2f169b66836f85ba161a6fc96b4f
fetched_at: '2026-06-28T22:46:31.257982+00:00'
product: rm
section_id: 6045459696023
source: central-rm
title: RH - RM - PTO - Avisos Calculados
type: support-article
updated_at: '2025-05-23T12:11:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26355201093271-RH-RM-PTO-Avisos-Calculados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26355263976727) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Quais são os avisos calculados disponíveis na janela de informações do espelho do cartão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto -A partir da versão 12.1  
  
**Solução**O sistema dispõe dos seguintes tipos de avisos calculados:

1. Tempo Mínimo Entre Jornadas (Inter jornada): Alerta quanto ao cumprimento de horas de Inter jornada foca disponível no parametrizador do Funcionário.

2. Horas trabalhadas superior a 10 horas: Alerta quanto aos dias com execução de carga horária superior a 10 horas....  
3. Menos que 1 hora de Refeição: Alerta quanto aos dias em que não foram cumpridas pelo menos uma hora de refeição. Este tipo de aviso é específico para horários onde há o registro de ausência planejada como os horários flexíveis.  
4. Horas trabalhadas sem intervalo de Refeição: Alerta quanto aos dias em que não foram efetuadas batidas de refeição.  
5. Batidas sem Pares correspondentes: Alerta para dias em que as batidas efetuadas não contenham paridade.  
6. Funcionário Afastado: Alerta quando o funcionário está com situação de afastamento.  
7. Funcionário de férias: Alerta quando o funcionário está com situação de férias.  
8. Funcionário Inativo: Alerta quando o funcionário está inativo.  
9. Tempo menor que o mínimo do intervalo com tempo planejado: Alerta quanto ao tempo executado de planejado é menor que o mínimo definido no horário.  
10. Semana não possui 24 horas contínuas de descanso: Alerta quando na definição do horário existe descanso menores que 24 horas e/ou descansos não contínuos. Essa validação é feita de acordo com o horário e não com as batidas efetuadas.

É possível consultar os avisos gerados no produto através dos seguintes menus abaixo:

Menu **Movimento | Aviso Calculado**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29419209162775)

Através da visão do Espelho de Ponto do funcionario, na guia **Avisos** em janela de informações:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29419209166359)

Através do **Relatório de Exceções**, para orientações de como gera-lo acesse o link abaixo:

[RH - RM - PTO - Relatório de exceções](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048567833)

**Importante**A tabela do banco de dados que armazena essas informações é a AAVISOCALCULADO.

**Saiba Mais**Para maiores informações sobre avisos calculados acesse o documento [Avisos Calculados](https://tdn.totvs.com/display/public/LRM/Avisos+Calculados)
