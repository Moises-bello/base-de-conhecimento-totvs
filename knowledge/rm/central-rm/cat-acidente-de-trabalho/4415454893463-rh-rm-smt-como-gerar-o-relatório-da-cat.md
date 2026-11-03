---
article_id: 4415454893463
category: CAT / Acidente de trabalho
content_hash: e232c8f120a873ac64d003251e41e41f6a860cad264f51b53fe775e9e805fdf4
fetched_at: '2026-06-28T22:47:37.007651+00:00'
product: rm
section_id: 1500000835021
source: central-rm
title: RH - RM - SMT - Como gerar o Relatório da CAT
type: support-article
updated_at: '2025-04-22T16:31:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415454893463-RH-RM-SMT-Como-gerar-o-Relat%C3%B3rio-da-CAT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16035449692951) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como gerar o relatório CAT(Ocorrência de Acidente de Trabalho)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Segurança e Saúde Ocupacional - Todas as versões.   
  
**Solução**Para gerar o relatório da CAT, siga os passos abaixo:   
   
**1.** Acesse o book no RM | Gestão | TOTVS Compartilhamento e baixe as seguintes estruturas:

**RHUREL0014 - 09.006.001 - CAT - Acidente de Trabalho (SQL)** para base **SQL**

**RHUREL0014 -09.006.003 - CAT - Acidente de Trabalho (Oracle)** para base **Oracle**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27047970460567)

**2.** Acesse o menu **Gestão | RM Reports** e vá em **Processos | Importar Estrutura de Relatório.**

***Obs: Antes importar a estrutura, valide se não há outra estrutura já importada com a mesma definição (CAT).***

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27047981583639)**

**3.** Será aberta uma janela para localização do relatório nas pastas do computador local. Abra a pasta pela janela que foi aberta e selecione o relatório desejado para realizar a importação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27047981584535)

**4.** Para finalizar a importação do relatório o sistema apresentará a tela acima. O campo **Código do relatório** apresenta o código do relatório selecionado, o campo **Sistema para importação** aponta qual é o módulo para onde o relatório será disponibilizado e por último a Flag **Sobrescrever Existente**é marcada automaticamente quando o sistema identifica que o relatório selecionado para importação já existe no sistema. As informações dos campos são preenchidas automaticamente pelo sistema e não precisam de alterações.  
  
**5.** Para gerar o relatório, acesse o módulo **Segurança e Saúde Ocupacional,** menu **Gestão** | **RM Reports** e expanda a árvore do módulo de **TOTVS Gestão de Pessoas** e selecione o relatório de CAT. E acesse o menu **Processos** | **Gerar Relatório**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27047981585559)

Deve ser passado os parâmetros necessários para geração da CAT correta, como **Cód Coligada**, **Cód Ocorrência** e **Local e data do acidente**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27047970471063)

O relatório também poderá ser incluído diretamente na visão da CAT para sua geração em **CAT/Incidentes** | **Ocorrências Acidente Trabalho** | **Anexos** | **Relatórios** | **Inserir relatório**:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27047970490391)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27047970493719)

1. Na etapa de Vínculo de Campos, deve preencher os parâmetros da Coligada e Ocorrência.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27047981611031)

**2.** Na etapa Definição de Grupos de Visualização, deve selecionar os perfis/usuários que terão acesso a este relatório na visão dos anexos ou se estará disponível para todos e execute até o final.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27047981613591)

**3.** Para gerar o relatório nesta visão, deve informar apenas o Local e data do acidente antes de submeter para geração:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27047981616535)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27047981619095)

**Saiba Mais**

Para maiores informações, acesse:

- [RH - RM - SMT - Dúvidas frequentes: CAT (evento S-2210)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24475175102871)

- [RH - RM - SMT - Importação de relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409650455703)
