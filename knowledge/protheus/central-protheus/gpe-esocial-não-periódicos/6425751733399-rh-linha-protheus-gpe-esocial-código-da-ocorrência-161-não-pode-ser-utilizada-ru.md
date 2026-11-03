---
article_id: 6425751733399
category: GPE - eSocial - Não Periódicos
content_hash: b64857fa9372150b80cb1bd6817399b2394bf578e1e7e7b544ce46ad3ec2caa2
fetched_at: '2026-06-28T22:45:04.350421+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - Código da Ocorrência: 161 Não pode ser
  utilizada rubrica cuja [natRubr] em S-1010 seja igual a [1801, 9220], desde que
  mes/ano da data do desligamento ou termino ou período de apuração seja maior ou
  igual a 01/07/21'
type: support-article
updated_at: '2026-06-16T12:50:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6425751733399-RH-Linha-Protheus-GPE-eSocial-C%C3%B3digo-da-Ocorr%C3%AAncia-161-N%C3%A3o-pode-ser-utilizada-rubrica-cuja-natRubr-em-S-1010-seja-igual-a-1801-9220-desde-que-mes-ano-da-data-do-desligamento-ou-termino-ou-per%C3%ADodo-de-apura%C3%A7%C3%A3o-seja-maior-ou-igual-a-01-07-21
---

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25790430493719)**Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Envio do evento **S-1200** retorna o **código de ocorrência**: "Código da Ocorrência: 161 - Descrição: Não pode ser utilizada rubrica cuja [natRubr] em S-1010 seja igual a [1801, 9220], desde que mês/ano da data do desligamento ou termino ou período de apuração seja maior ou igual a [01/07/2021]."  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

O erro ocorre quando a natureza de rubrica enviada através da tag **natRubr** do **S-1010** está com validade expirada ou o código está incorreto:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25790458556823)

Desde o dia **23/05/2022** passou a ser obrigatório o envio dos eventos no **Leiaute Simplificado S-1.0**. Neste Leiaute, **algumas naturezas de rubricas constam como expiradas**, conforme Anexo I do Leiaute S-1.2.

Exemplo:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25790526769559)

Nesse caso deve ser identificado quais são as rubricas que estão com estas naturezas e realizar o ajuste para **naturezas válidas** conforme a **tabela 03** do leiaute do eSocial: [Tabela 03 - Natureza das Rubricas da Folha de Pagamento](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-nt-02-2024/tabelas.html#03).  
  
Para ajustar a **Natureza** de cada verba identificada:

**1.** Acesse o **cadastro de verbas** (tabela SRV) em **Atualizações > Definição Calculo > Verbas**;  
**2.** Clique em **alterar** na verba identificada vinculada à natureza expirada;  
**3.** Na **aba eSocial** acesse o **campo Natureza** e altere conforme as naturezas válidas de acordo com a tabela 03 do leiaute simplificado.  
  
**Por exemplo:** o código 1801 tem data término preenchida, dessa maneira essa natureza não deve ser

mais utilizada.  
  
**Atenção ao confirmar a alteração**, pois o sistema perguntará a competência. Exemplo, se informado 06/2022 o sistema e o esocial entenderão a alteração somente para eventos enviados da competência 06 ou posterior.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7215914967831)

Veja o boletim técnico: <https://tdn.totvs.com/pages/releaseview.action?pageId=630365963#beneficios-VRF>

**Saiba Mais**  
[RH - Linha Protheus - GPE - eSocial - S-2230 - Código da Ocorrência: 8 - Descrição : Grupo #39;Informacoes referentes ao período aquisitivo de ferias#39; deve ser preenchido. Verifique as condições de preenchimento no leiaute.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6391696659223)  
[RH - Linha Protheus - GPE - eSocial - S-2299 - Como retificar uma rescisão através do SIGAGPE sem precisar excluir o calculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020865371)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina no Portal do cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991-Carolina-Assistente-Virtual-Como-usar-a-Carolina-no-Portal-do-cliente?source=search)
