---
content_hash: 114ff12a0cfc6f0dbc1f1580cc842c68c8b1ae29d4ce1966633652548191242c
fetched_at: '2026-06-29T00:08:23.448593+00:00'
page_id: '270088132'
product: rm
source: tdn-rm
title: Utilizar novo conceito. Conexões de Origem (TXT) / Conexões de destino (Banco
  de Dados).
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270088132
version: 19
---

# Índice:

---

.\*ndice:

# Objetivo:

---

   O objetivo deste documento é mostrar como inserir dados em uma tabela criada pelo metadados a partir de um arquivo TXT.

# Procedimento:

---

    No vídeo abaixo realizo a criação de uma tabela através da ferramenta de metadados e realizo o processo ETL via conceito, utilizando como conexão de origem um arquivo TXT e como conexão de destino a tabela que foi criada via metadados.

Download do vídeo:

Atenção

Observação: Recomendamos que na importação de arquivos .txt utilize a configuração do arquivo:

Exemplo simples de processo ETL. Conceito é uma ferramenta para importação e exportação de dados do sistema. Possuindo varias conexões de origem e destino assim como "Arquivo Texto, Arquivo XML, Banco de dados, Data Server RM.NET, DLL.Net, Microsoft CRM e Web Service".

Não devem ser usados caminhos de arquivo referentes a **unidades de rede mapeadas**. Deve ser usado o caminho do arquivo local em ambiente local e o caminho de rede nos ambientes distribuídos.

Em ambientes **tenantizados**. Deve ser usado o caminho relativo, do arquivo ou diretório.  
*Lembrando que o arquivo ou diretório selecionado deve existir no local indicado dentro da estrutura do tenant.*

Atenção

## Importação de Dados para o Sistema RM

Para facilitar a importação de dados no sistema RM, é possível utilizar um arquivo de texto. No entanto, o sistema importa todo o conteúdo do arquivo, incluindo possíveis cabeçalhos. Para solucionar esse problema, foi adicionado o campo "Linha Inicial", que permite definir a partir de qual linha os dados serão importados.

### Como Utilizar o Campo "Linha Inicial"

O campo "Linha Inicial" especifica a linha a partir da qual a importação de dados deve começar, ignorando as linhas anteriores. Veja abaixo como configurar esse campo:

* **Linha Inicial = 1**: A importação começará a partir da primeira linha do arquivo, não ignorando nenhuma linha.
* **Linha Inicial = 2**: A importação começará a partir da segunda linha do arquivo, ignorando a primeira linhas (Possíveis cabeçalhos).

### Exemplo

Se você tiver um arquivo com o seguinte conteúdo:

Nome, Idade, Cidade  
João  ,   25   , São Paulo  
Maria,   30   , Rio de Janeiro  
Pedro,   22   , Belo Horizonte

E configurar o campo "Linha Inicial" como 2, o sistema ignorará a primeira linha (que contém possíveis cabeçalhos) e importará apenas os dados:  
  
João  ,   25   , São Paulo  
Maria,   30   , Rio de Janeiro  
Pedro,   22   , Belo Horizonte

### Benefícios

* **Precisão**: Importa apenas os dados necessários, sem incluir o cabeçalho.
* **Flexibilidade**: Permite definir a linha inicial conforme a estrutura do seu arquivo.

### Considerações Finais

Certifique-se de ajustar corretamente o campo "Linha Inicial" conforme a estrutura do seu arquivo de texto para garantir que apenas os dados desejados sejam importados para o sistema RM.

falsefalse

**Produto:** Framework

false

**Versão:** 11.XX; 12.1.XX

false

**Processo:** Incluindo dados em uma tabela criado pelo metadados via conceito.

falsefalse

**Status:** Finalizado
