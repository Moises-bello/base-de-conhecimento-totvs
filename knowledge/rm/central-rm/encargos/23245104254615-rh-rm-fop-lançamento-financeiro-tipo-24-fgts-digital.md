---
article_id: 23245104254615
category: Encargos
content_hash: e1a680eaf963dee284b57c03dda35d050f451b366599d62bfbb69c96872e62ce
fetched_at: '2026-06-28T22:46:52.266846+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Lançamento financeiro tipo 24 -  FGTS DIGITAL
type: support-article
updated_at: '2024-06-11T13:38:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23245104254615-RH-RM-FOP-Lan%C3%A7amento-financeiro-tipo-24-FGTS-DIGITAL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23245073557911) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar lançamento financeiro do tipo **24 - FGST Digital**?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos *Patches* 12.1.2306.254, 12.1.2310.198 e 12.1.2402.138

**Solução**Com a introdução do FGTS Digital, tornou-se necessário dissociar a geração do lançamento financeiro dos processos da SEFIP e GRRF. Isso exigiu a criação de um novo tipo de lançamento financeiro denominado **24-Total Guia FGTS Digital.**

Os **desligamentos** que ocorrem **a partir de 01/03/2024**, o recolhimento do FGTS Mensal, Rescisório e Indenização Compensatória (multa do FGTS) passam a ser **através do FGTS Digital**, não existindo mais a nomenclatura GRRF – Guia de Recolhimento Rescisório do FGTS. A guia passa a ser chamada de **GFD – Guia do FGTS Digital**.

Para composição dos valores a serem gerados, o sistema irá calcular os valores do FGTS folha, FGTS 13o. Terceiro e FGTS Indenizado.

* **Tratativa realizada no produto**

***Atenção**: Após a atualização da versão será necessário executar o sistema **RM.Atualizador.exe** para a criação do novo tipo de lançamento financeiro.*

Criado o tipo de lançamento **24-Total Guia FGTS Digital**, para atender o cálculo da guia do FGTS Digital.

Pontos de destaque:

- Serão considerados os **códigos de cálculos 27** e **148** para buscar o mês anterior a demissão.  
- Quando houver **retificação da rescisão** ou **pagamento após a rescisão**, os valores serão enviados no tipo **Mensal**, conforme descrito no site Perguntas e Respostas 04.09.  
- A quebra na geração será de acordo com os **parâmetros de seleção** do processo do Lançamento Financeiro.  
- Quando o lançamento financeiro for **agrupado por lotação tributária** (tomador de serviço), é fundamental **executar o Relatório de Conferência de FGTS** para alimentar a tabela ***PESOCIALTOTAISLOTACAO***. Isso é essencial para evitar problemas de desempenho na geração do lançamento. Caso essa etapa não tenha sido realizada, ao gerar o lançamento financeiro, será exibida a seguinte mensagem: ***O lançamento "Total Guia FGTS Digital" está parametrizado por lotação tributária, é preciso executar o Relatório de Conferência de FGTS antes de gerar o lançamento para a chapa XXX**.*

Será possível definir o **tipo de lançamento** a ser realizado, conforme descrito no [Manual de Orientação do FGTS DIGITAL - Página 80](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-do-orientacao-do-fgts-digital-versao-1-1-01-03-2024.pdf), podendo ser parametrizado conforme abaixo:

**• Mensal**  
Ao selecionar esse tipo, o sistema irá gerar o lançamento considerando **todos os funcionários**, inclusive demitidos, com **exceção dos demitidos com os tipos de demissão com direito a saque** de FGTS.

**• Rescisório**Ao selecionar esse tipo, o sistema irá gerar o lançamento considerando todos os funcionários **demitidos com o tipo de demissão que tem direito a saque** de FGTS e que possuem o parâmetro **FGTS Mês anterior será recolhido na GRRF/FGTS Digital** desmarcado na rescisão.

**• Rescisório + Mensal**

Ao selecionar esse tipo, o sistema irá gerar o lançamento considerando todos os funcionários **demitidos com o tipo de demissão que tem direito a saque** de FGTS e que possuem o parâmetro **FGTS Mês anterior será recolhido na GRRF/FGTS Digital** marcado na rescisão, considerando o mês da demissão e o mês anterior a demissão. Esta geração é necessária para atender a situação descrita no **Manual de Orientação do FGTS DIGITAL - Página 80**, já citada.

**Saiba mais**  
Para mais informações, acesse:

* [DT - FGTS Digital - Lançamento Financeiro](https://tdn.totvs.com/pages/viewpage.action?pageId=834247089#Aba1-2)
