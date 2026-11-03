---
article_id: 360051486074
category: RH - Cálculo Adiantamento
content_hash: 058aeb3f886ad519f8a3fde8c0e7bcf65ecb00ee11648451c927800145f8f435
fetched_at: '2026-06-28T22:43:14.320972+00:00'
product: protheus
section_id: 360011983213
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de Adiantamento não apresenta verbas de
  líquido para geração de arquivo CNAB e Relatório de Líquidos (GPER020)
type: support-article
updated_at: '2025-04-15T18:11:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051486074-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Adiantamento-n%C3%A3o-apresenta-verbas-de-l%C3%ADquido-para-gera%C3%A7%C3%A3o-de-arquivo-CNAB-e-Relat%C3%B3rio-de-L%C3%ADquidos-GPER020
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24798164194967)**Tempo aproximado para leitura:**00:01:00 min**

**Ocorrência**Após processamento, o cálculo de Adiantamento não apresenta verbas de líquido para geração de arquivo CNAB e Relatório de Líquidos (GPER020).  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Causa**A sequência de Cálculo 00620 no Roteiro de Cálculo ADI, onde trata a gravação de líquido está desabilitada.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. **Acesse Atualizações -> Definições de Cálculo -> Roteiros de Cálculo** e selecione o roteiro ADI:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31434639417111)

2. Dentro do roteiro ADI, busque a sequência de **cálculo 00640** - Grava Líquido e Arredondamento e configure a Fórmula **S\_ADILIQ / HABILITADO = "SIM"**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31434639422103)  
  
3) Após essa alteração, clique em **Confirmar**, acesse a rotina de cálculo e refaça o processo de cálculo do adiantamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31434639424791)

**Saiba Mais:**

[Gestão de Pessoas (SIGAGPE)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000926522-Gest%C3%A3o-de-Pessoas-SIGAGPE)

[MP - GPE - Rotina CNAB (GPEM080) cria uma linha vazia no final do arquivo mesmo configurado como "Linha vazia no fim do arquivo = Não"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051977133-MP-GPE-Rotina-CNAB-GPEM080-cria-uma-linha-vazia-no-final-do-arquivo-mesmo-configurado-como-Linha-vazia-no-fim-do-arquivo-N%C3%A3o-?source=search)  
[MP - GPE - Variáveis para configuração do layout de arquivo CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026143934-MP-GPE-Vari%C3%A1veis-para-configura%C3%A7%C3%A3o-do-layout-de-arquivo-CNAB?source=search)  
[MP - GPE - Função para gerar sequência numérica referente ao lote do CNAB da Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018993471-MP-GPE-Fun%C3%A7%C3%A3o-para-gerar-sequ%C3%AAncia-num%C3%A9rica-referente-ao-lote-do-CNAB-da-Folha-de-Pagamento?source=search)  
[MP - GPE - Parâmetro Processar Banco na geração do Arquivo CNAB (GPEM080)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024630454-MP-GPE-Par%C3%A2metro-Processar-Banco-na-gera%C3%A7%C3%A3o-do-Arquivo-CNAB-GPEM080-?source=search)  
[MP - GPE - Como configurar a inclusão de Segmento B no layout do arquivo CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028474032-MP-GPE-Como-configurar-a-inclus%C3%A3o-de-Segmento-B-no-layout-do-arquivo-CNAB?source=search)
