---
article_id: 360050629074
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 5228c3aceda99701cbcb65848aacf15b9fe4d4d2dcbf6ab6d4e2b6b0fc017a76
fetched_at: '2026-06-28T22:42:07.804544+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GIA-SP - 4º
  Passo - Extrator Fiscal
type: support-article
updated_at: '2024-06-04T19:08:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050629074-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GIA-SP-4%C2%BA-Passo-Extrator-Fiscal
---

**Ocorrência**

Necessário atualizar o ambiente TAF para utilização da GIA-SP.

**Ambiente**Protheus - Livros Fiscais – A partir da versão 12.1.17  
 **Causa**Necessidade das configurações para a geração do arquivo da **Nova GIA**através do **TAF.**

**Solução**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402488106007)**

**Livros Fiscais -> Miscelânea -> Arq. Magnéticos -> Extrator Fiscal (EXTFISXTAF)**.

A execução do **Extrator Fiscal** é de extrema importância pois, é nele que irá buscar as informações geradas no Fiscal no período desejado e é nele que irá alimentar a tabela Auxiliar do **TAF (TAFST2)**.

**OBS**.: Todos os registros devem ser integrados, para correta geração da **GIA**.

**OBS 2**: O extrator fiscal, a partir do mês 03/2020, gera os dados diretamente na TAFST2 para clientes que utilizam o TAF como módulo. A TAFST1 não é utilizada na integração de clientes que usam o Protheus e TAF como módulo do Protheus.

![](https://totvssuporte.zendesk.com/attachments/token/WpFYuIlps6iwR3QVNHZH14vns/?name=inline2014798910.png)

Atenção aos parâmetros a serem preenchidos na *Wizard* do **Extrator Fiscal**.

Pasta: **Geração**

**Data de?** = Obrigatório conter o período de extração preenchido.

**Data até?** = Obrigatório conter o período de extração preenchido.

**Tipo de Saída?** = Banco a Banco.

**Deseja integrar?**1- Somente cadastros:  **(Serão extraídos todos os cadastros presentes no Layout TAF, sendo necessário selecionar os cadastros específicos para a GIA-SP)** Utilize esta opção para carga inicial no **TAF**, sendo necessário executa-la uma única vez. 2**-**Somente Movimentos:  **(Serão extraídos todos os movimentos presentes no Layout TAF, sem opção de selecionar um movimento específico)**  
3**-**Ambos: **(Serão apresentados todos os cadastros e movimentos presentes no Layout TAF, sendo possível selecionar os cadastros e movimentos a serem gerados)** Lembramos que ao selecionar os cadastros presentes nesta opção, serão considerados apenas os cadastros realizados dentro do período de extração dos dados.

![](https://tdn.totvs.com/download/attachments/379308197/image2019-7-31_18-37-11.png?version=1&modificationDate=1564609031833&api=v2)

**Filtra Apenas Reinf?**Para extrair as informações para a GIA, preencher = 2- NÃO.

Pasta:**Movimento**

Tipo de Movimento? = 1-Ambos

Nota Fiscal de? = BRANCO

Nota Fiscal até? = ZZZZZZ

Serie de? = BRANCO

Serie até? = ZZZ

Pasta: **Apuração / SPED**

Centralizar apurações e totalizadores em uma única filial? = 1-Não

**Observação:**

No processo do Extrator Fiscal, caso seja a primeira vez que está fazendo a extração de dados para o  modulo do **TAF**, importante fazer a primeira carga no **TAF**, com os *Layouts* de cadastros como parâmetro, com um intervalo entre a data inicial e final que pegar todos os dados cadastrais do **Protheus** para alimentar as tabelas do **TAF**, exemplo data inicial: 01/01/1970 até a data atual, marcando somente os *Layouts* de Cadastros.

Abaixo relação dos Layout essenciais para geração da GIA:  
  
Selecione os *Layouts* de Cadastros  **T001AE, T003, T005, T006, T007, T009, T010 e T011** com as perguntas:

**Deseja integrar**:  1 - Somente Cadastros

**Filtra Reinf**: 2 - Não

Após a **Extração Fiscal** ser concluída para os *Layouts* de cadastro acima, execute a rotina de processamento, conforme passo **5-Processamento** e **6-Gerenciador de Integração.**

Após concluir o ajuste das inconsistências (se houverem) apresentadas no gerenciador de integração, conforme passo 6, realize a extração fiscal dos movimentos **T013, T020 e T021** com as perguntas:   
  
**Deseja integrar**: 3 - Ambos

**Filtra Reinf**: 2 - Não

**Observação:**Para as entregas dos meses seguintes da **GIA-SP**, basta realizar a extração com a pergunta **Deseja integrar**: Ambos e marcar tanto os *Layouts* de **cadastro** quanto os de **movimento**, pois serão considerados somente os cadastros realizados dentro do período. Desta forma, garantiremos que não faltem dados inclusos recentemente para entrega da obrigação fiscal no **TAF** e não ocorrerá erros na falta de algum cadastro novo.

*Layouts*: **T001AE, T003, T005, T006, T007, T009, T010, T011, T013, T020 e T021.**

Após a**Extração Fiscal** ser concluída para os *Layouts* acima, execute a rotina de processamento, conforme passo **5-Processamento** e **6-Gerenciador de Integração**
