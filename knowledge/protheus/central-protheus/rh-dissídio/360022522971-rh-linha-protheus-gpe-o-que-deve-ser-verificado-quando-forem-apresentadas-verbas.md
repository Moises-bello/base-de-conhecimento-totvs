---
article_id: 360022522971
category: RH - Dissídio
content_hash: 7ea8cb6630e0be9b13dab1090a7256617859c5204d64829e0ea12a3b67139a4e
fetched_at: '2026-06-28T22:43:43.409671+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - O que deve ser verificado quando forem apresentadas
  verbas de DSR com valores negativos no cálculo do Dissídio
type: support-article
updated_at: '2025-09-09T12:21:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022522971-RH-Linha-Protheus-GPE-O-que-deve-ser-verificado-quando-forem-apresentadas-verbas-de-DSR-com-valores-negativos-no-c%C3%A1lculo-do-Diss%C3%ADdio
---

#### time.png Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**O que deve ser verificado quando forem apresentados verbas de DSR com valores negativos no cálculo do dissídio  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**

1. Verifique se o cadastro de períodos é compartilhado;  
2. Caso seja, **verifique se houve manipulação** dos dias trabalhados e dias DSR na aba Cadastro do Calendário (estas informações não devem ser alteradas durante o período com cálculos já executados pois ocasionará erro no cálculo do dissídio);  
3. Neste caso, sugerimos utilizar as tabelas de cadastro de períodos de forma exclusiva.

4. Identificada a manipulação no cadastro do período, para correção sem ajuste nas tabelas para que permaneçam com a mesma configuração do cálculo inicial, somente lançando o valor correto no campo informado na MANUTENÇÂO da rotina de dissídio.

**Importante:**  
- As verbas de horas extras não devem conter identificador de cálculo;  
- Verbas do tipo valor com **Sim** para dissídio e sem ID de cálculo, devem ser configurados também com **Sim** no campo Recal.Lan.VL (cadastro de verbas - aba dissidio);

Dica: confira o valor da verba atual, para entender o cálculo executado. Depois de conferir o valor, fazer o mesmo cálculo para a verba da SRD usando salário da época.  
  
**Saiba Mais**[MANUAL GPE - Dissídio Retroativo](https://tdn.totvs.com/pages/viewpage.action?pageId=220889925)

**DSR na Folha de Pagamento**  
[RH - Linha Protheus - GPE - Cálculo de DSR para funcionário intermitente considerando o mês completo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035975093-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-DSR-para-funcion%C3%A1rio-intermitente-considerando-o-m%C3%AAs-completo?source=search)  
[RH - Linha Protheus - GPE - Cálculo de horas extras e DSR rateados automaticamente através da rotina de lançamentos mensais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016010332-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-horas-extras-e-DSR-rateados-automaticamente-atrav%C3%A9s-da-rotina-de-lan%C3%A7amentos-mensais?source=search)  
[RH - Linha Protheus - GPE - Sistema calcula automaticamente desconto de DSR falta quando lançada verba de ID 0054-Falta](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050719274-RH-Linha-Protheus-GPE-Sistema-calcula-automaticamente-desconto-de-DSR-falta-quando-lan%C3%A7ada-verba-de-ID-0054-Falta?source=search)  
[RH - Linha Protheus - GPE - Como realizar o cálculo do DSR de horistas conforme a tabela de Horário Padrão do módulo SIGAPON](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018862371-RH-Linha-Protheus-GPE-Como-realizar-o-c%C3%A1lculo-do-DSR-de-horistas-conforme-a-tabela-de-Hor%C3%A1rio-Padr%C3%A3o-do-m%C3%B3dulo-SIGAPON?source=search)  
[RH - Linha Protheus - GPE - De onde o sistema busca os dias para cálculo de DSR de hora extra, adicional noturno e outros DSRs?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047913534-RH-Linha-Protheus-GPE-De-onde-o-sistema-busca-os-dias-para-c%C3%A1lculo-de-DSR-de-hora-extra-adicional-noturno-e-outros-DSRs?source=search)  
[RH - Linha Protheus - GPE - Como o sistema calcula a quantidade de horas/referência do DSR sobre as Horas Extras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057485413-RH-Linha-Protheus-GPE-Como-o-sistema-calcula-a-quantidade-de-horas-refer%C3%AAncia-do-DSR-sobre-as-Horas-Extras?source=search)  
[RH - Linha Protheus - GPE - Documentação utilizada como referência para definir as fórmulas de cálculo (DSR, 13º, férias, etc) para os funcionários com contrato intermitente tendo como embasamento a legislação da reforma trabalhista?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025423474-RH-Linha-Protheus-GPE-Documenta%C3%A7%C3%A3o-utilizada-como-refer%C3%AAncia-para-definir-as-f%C3%B3rmulas-de-c%C3%A1lculo-DSR-13%C2%BA-f%C3%A9rias-etc-para-os-funcion%C3%A1rios-com-contrato-intermitente-tendo-como-embasamento-a-legisla%C3%A7%C3%A3o-da-reforma-trabalhista?source=search)  
[RH - Linha Protheus - GPE - Como calcular DSR para Tarefeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021010632-RH-Linha-Protheus-GPE-Como-calcular-DSR-para-Tarefeiro?source=search)  
   
**DSR na Rescisão**  
[RH - Linha Protheus - GPE - Calculo DSR horista variável em rescisão, quando o id 0048 é lançado manualmente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051437814-RH-Linha-Protheus-GPE-Calculo-DSR-horista-vari%C3%A1vel-em-rescis%C3%A3o-quando-o-id-0048-%C3%A9-lan%C3%A7ado-manualmente?source=search)  
[RH - Linha Protheus - GPE - Como proporcionalizar o DSR no cálculo da rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021567112-RH-Linha-Protheus-GPE-Como-proporcionalizar-o-DSR-no-c%C3%A1lculo-da-rescis%C3%A3o?source=search)  
[RH - Linha Protheus - GPE - Por que rescisão complementar para pagamento de comissão calcula o DSR com base no calendário da rescisão original](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008819222-RH-Linha-Protheus-GPE-Por-que-rescis%C3%A3o-complementar-para-pagamento-de-comiss%C3%A3o-calcula-o-DSR-com-base-no-calend%C3%A1rio-da-rescis%C3%A3o-original?source=search)  
[RH - Linha Protheus - GPE - Por que relatório de médias emitido no cálculo da rescisão apresenta linha com descrição TOT DSR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12712849650711-RH-Linha-Protheus-GPE-Por-que-relat%C3%B3rio-de-m%C3%A9dias-emitido-no-c%C3%A1lculo-da-rescis%C3%A3o-apresenta-linha-com-descri%C3%A7%C3%A3o-TOT-DSR?source=search)  
   
**DSR nas Férias**  
[RH - Linha Protheus - GPE - Como calcular o DSR sobre médias no cálculo das férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418618747799-RH-Linha-Protheus-GPE-Como-calcular-o-DSR-sobre-m%C3%A9dias-no-c%C3%A1lculo-das-f%C3%A9rias?source=search)
