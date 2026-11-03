---
content_hash: 931f34110b8653d92c64993c45536d69a510a25beb3eb96c9773bfbcb01d4083
fetched_at: '2026-06-29T00:06:14.476758+00:00'
page_id: '210046356'
product: rm
source: tdn-rm
title: Importação de CEP's
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=210046356
version: 33
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

A importação de CEP é uma operação de inserção na base de dados do DNE (Diretório Nacional de Endereços), que é um banco de informações disponibilizado pelos Correios em arquivos. Para download dos arquivos acesse o site onde é possível obtê-los gratuitamente para teste.

       O CD a ser adquirido nos correios é o de BASE DE DADOS COMERCIAL DO DNE (DNE – Diretório Nacional de Endereços).

        Ao realizar a instalação do aplicativo dos correios, este irá criar uma pasta chamada Base\_eDNE, onde conterá duas sub-pastas, GU e TE.

        Serão utilizados para importação somente os arquivos com extensão TXT que constam na pasta \Basico\Delimitado (LOG\_BAIRRO.TXT, LOG\_CPC.txt, LOG\_LOCALIDADE.TXT, etc.).

        Os dados serão armazenados nas tabelas GCEPESPECIAL, GLOGRADOURO, GLOCALIDADE e GBAIRRO.

        Os Correios disponibilizam uma versão de demonstração do DNE que contém uma faixa limitada de CEP’s. Uma vez instalada esta versão, você poderá importar os CEP’s para o sistema, a fim de avaliar o funcionamento do recurso de localização de CEP’s.

Isenção de responsabilidade para links externos

Esses links são fornecidos como uma conveniência e apenas para fins informativos; eles não constituem um endosso ou uma aprovação pela TOTVS de qualquer um dos produtos, serviços ou opiniões da corporação ou organização ou indivíduo, bem como a manutenção e disponibilidade dos mesmos.

[Clique aqui para acessar a página dos correios e baixar a versão de demonstração](https://www.correios.com.br/enviar/marketing-direto/arquivos)

## **02. EXEMPLO DE UTILIZAÇÃO**

**Acesse**: Serviços globais | Serviços |  Utilitários | Importação de CEP

Para realizar a importação basta localizar os arquivos no disco e selecionar a forma de importação, se você quer sobrepor alguma importação já existente ou manter os dados da base e importar novos registros.

 As opções para importação comportam da seguinte maneira:

* "Sobrepõe o registro da base de dados com as informações do novo registro"  
  Insere novos registros na base de dados e Sobrepões os registros já existentes.  
  Utiliza os arquivos iniciados com "LOG", que são arquivos disponibilizados pelo correio do DNE.  
  Exemplo Arquivo: LOG\_LOCALIDADE  
  Indicado quando você deseja importar novos registros e alterar os registros já existentes na base de dados.

* "Mantém o registro da base de dados inalterado"  
  Insere novos registros na base de dados e não altera os registros já existentes.  
  Utiliza os arquivos iniciados com "LOG", que são arquivos disponibilizados pelo correio do DNE.  
  Exemplo Arquivo: LOG\_LOCALIDADE  
  Indicado quando você deseja importar novos registros sem alterar os registros já existentes na base de dados.

* "Atualização através de arquivo delta"  
  Insere novos registros na Base de dado e atualiza os registros já existentes.  
  Utiliza os arquivos iniciados com "DELTA", que são arquivos disponibilizados pelo correio para atualizar o DNE.  
  Exemplo Arquivo: DELTA\_LOG\_LOCALIDADE  
  Indicado quando você deseja importar novos registros e alterar os registros já existentes na base de dados através dos arquivos de atualização do DNE que iniciam com "DELTA" e que são disponibilizados pelos correios.

        Ao final do processo será exibido um log informando o que ocorreu na importação e se houve algum empecilho.

DICA:

A importação é um processo que pode ser executado na hora ou agendado (se o ambiente for três camadas). Para importar é necessário informar um diretório compartilhado com todos os usuários, lembrando que este diretório deve ser acessível pelo servidor de aplicação (local onde o Host é executado).

ATENÇÃO:

Erros de dados no arquivo podem impedir a continuação do processo.

# Orientações importantes

---

        No site dos [CORREIOS](https://www.correios.com.br/enviar/marketing-direto/saiba-mais-nacional), localize na aba Arquivos os itens para download para realizar testes, conforme exemplificado na imagem abaixo:

        Ao realizar o download dos Arquivos para Atualização no site dos Correios, os mesmos apresentarão a informação "DELTA" no nome do documento .txt:

        Para realizar o teste neste formato, deverá acessar a opção de Importação: **Atualização através de arquivos DELTA**:

        Para realizar o teste/importação na opção **Sobrepõe o registro da base de dados com** **informações****do novo registro,** deve-se remover a palavra "DELTA" do nome dos arquivos, conforme mostrado a seguir:

false

**Versão:** 11.82.XX e 12.01.XX
