---
article_id: 28932276280855
category: Financeiro
content_hash: 6af1cc4aaabc6489ac15735420b371fa3b75e5cb79a1edf2e3da7a14e33d4a49
fetched_at: '2026-06-28T22:38:04.207280+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: ‭Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940- Criação dos
  campos FK5_MSUIDT e IG_MSUIDT
type: support-article
updated_at: '2025-01-02T20:37:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28932276280855--Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Cria%C3%A7%C3%A3o-dos-campos-FK5-MSUIDT-e-IG-MSUIDT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28932269173143) Tempo aproximado para leitura: 00**:05:00 min****Dúvida**CTBA940- Criação dos campos FK5\_MSUIDT e IG\_MSUIDT

**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - Financeiro - Todas as versões  
  
**Solução**

### 01. GERAR SDF COM CAMPOS DE ID

O objetivo da opção Gerar SDF com campos de ID é facilitar a criação dos campos de ID necessários para utilização do conciliador.

#### **01. RESUMO**

Esta opção fará a leitura das configurações contidas na tabela QLB e, com as tabelas de origem e destino encontradas, fará a sugestão para criação dos campos XXX\_MSUIDT, onde XXX representa o código da tabela utilizada na conciliação.

**Esta opção não irá criar os campos no banco**, ela ira gerar um arquivo SDF na pasta \systemload\ para posterior execução do **UPDDISTR**.

---

#### **02. GERANDO SDF**

Escolher a opção "**Gerar SDF com campos de ID**" e clicar no botão Avançar.

![](https://tdn.totvs.com/download/attachments/644712730/image2021-10-17_14-42-33.png?version=1&modificationDate=1634492554077&api=v2)

Será exibida a tela de apresentação da opção selecionada:

![](https://tdn.totvs.com/download/attachments/644712730/image2022-1-12_11-23-50.png?version=1&modificationDate=1641997430420&api=v2)

Ao clicar em avançar, o sistema fará a leitura das tabelas de origem e destino cadastradas da tabela QLB (Configurações de Match). Será sugerida a criação dos campos XXX\_MSUIDT dessas tabelas (onde XXX é o código da tabela encontrada).

Os campos já existentes na base de dados ficarão com o STATUS "OK" e não serão exportados para o SDF.

Os campos não encontrados, ficarão com o STATUS "Incluir" e serão exportados para o arquivo SDF.

Campos que serão criados com base nas tabelas encontradas no cadastro da QLB:

![](https://tdn.totvs.com/download/attachments/644712730/image2022-6-27_10-18-38.png?version=1&modificationDate=1660941656177&api=v2)

Clique em avançar para exportar o arquivo SDF para a pasta systemload:  
Caso já exista um arquivo diferencial nessa pasta, o sistema perguntará se deve sobrescrevê-lo.

![](https://tdn.totvs.com/download/attachments/644712730/image2022-1-12_11-26-12.png?version=1&modificationDate=1641997572820&api=v2)

Exemplo de arquivo criado na pasta systemload.

Evidência do arquivo manifest\_update com os detalhes do arquivo SDF gerado pela ferramenta.

![](https://tdn.totvs.com/download/attachments/644712730/image2022-1-12_11-30-2.png?version=1&modificationDate=1641997802837&api=v2)

Após confirmar a gravação do arquivo, o Wizard exibe a mensagem de SDF exportado com sucesso:

Clicando no botão finalizar desta opção, o sistema pergunta se deseja executar o UPDDISTR para criação dos campos:

![](https://tdn.totvs.com/download/attachments/644712730/image2022-1-12_11-26-50.png?version=1&modificationDate=1641997610437&api=v2)

Se clicar em Sim, o sistema redirecionará para execução do UPDDISTR

Se clicar em Não, o sistema finalizará esta etapa.

![](https://tdn.totvs.com/download/attachments/644712730/image2021-9-9_14-45-11.png?version=1&modificationDate=1634245818060&api=v2)

Ao finalizar esta etapa do Wizard, a mensagem de Processamento Finalizado é exibida:

![](https://tdn.totvs.com/download/attachments/644712730/image2021-10-17_14-36-41.png?version=1&modificationDate=1634495615257&api=v2)

**Documentação: <https://tdn.totvs.com/pages/viewpage.action?pageId=638741736>**
