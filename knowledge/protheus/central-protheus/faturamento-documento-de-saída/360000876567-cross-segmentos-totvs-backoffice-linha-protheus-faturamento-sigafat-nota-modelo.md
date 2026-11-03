---
article_id: 360000876567
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 4b9dfbb0e364da8d1e0e531434c5f97e75ff8acf4877d59ee98f19fc7efe33be
fetched_at: '2026-06-28T22:38:44.192660+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Nota modelo 21 e 22
type: support-article
updated_at: '2021-07-26T16:51:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000876567-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Nota-modelo-21-e-22
---

**Dúvida**

Quais são as particularidades da NF modelo 21 e 22?

**Ambiente**Cross Segmentos-TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT)-  todas as versões.

**Solução**

Dispõe sobre a uniformização e disciplina a emissão, escrituração, manutenção e prestação das informações dos documentos fiscais emitidos em via única por sistema eletrônico de processamento de dados para contribuintes prestadores de serviços de comunicação e fornecedores de energia elétrica.

Cada estado pode inserir em seu Regulamento do ICMS (RICMS-SP / PR / etc) detalhes da obrigatoriedade; porém, sempre com base no Convênio ICMS 115/2003

Mais informações sobre a Legislação: [Confaz - CONVÊNIO ICMS 115/03](https://www.confaz.fazenda.gov.br/legislacao/convenios/2003/cv115_03)

**A Emissão dessa Nota no sistema, até o momento da Preparação do Documento de Saída, segue o mesmo processo habitual (Pedido de Venda / Prepara Documento de Saída), sem tratativas próprias a este modelo (salvo necessidades específicas do cliente).**

Algumas particularidades:

**1- Transmissão:**Diferente do modelo 55; ***o modelo 21 / 22 não é******transmitido via TSS***, mas sim, ***via sintegra*** pelo sistema eletrônico de processamento de dados, obedecendo ao disposto na Portaria CAT nº 79/2003

O processo no Protheus é realizado na rotina Fiscal **Instr. Normativas (MATA950)** que atende ao Convênio 115.

**2-** **Numeração da Nota** Fiscal que periodicamente se reinicia (volta a numeração do “0”): Hoje, não possível reiniciar a mesma série, existe um projeto em andamento, pois se trata de uma alteração estrutural do sistema.

O que é possível fazer é tratar a questão no sistema. Deve-se alterar a série da nota sempre que a numeração tiver de se reiniciar (que também é um procedimento permitido – utilizar uma nova série). Assim, é possível ter notas com a mesma numeração se a série for outra.

**3-** **Série** **variável incremental:**Mesmo processo da alteração de número da série. Criação de série deve ser manual.

Mais informações e particularidades voltadas a essa modalidade de emissão, acesse: [Particularidades da NF modelo 21 e 22](http://tdn.totvs.com/display/PROT/FAT0023_Particularidades_da_NF_modelo_21_e_22)
