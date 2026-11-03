---
article_id: 360018817452
category: CRM - Vendas
content_hash: 317b5c43fe9c214d63befb0c2b5c8c3e98e763cbadd1565687efff345fca1f64
fetched_at: '2026-06-28T22:40:25.804420+00:00'
product: protheus
section_id: 1500001549102
source: central-protheus
title: Cross Segmentos - BackOffice Protheus  SIGACRM - Configuração de Integração
  Word na Oportunidade Vendas Int Word
type: support-article
updated_at: '2025-04-04T20:52:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018817452-Cross-Segmentos-BackOffice-Protheus-SIGACRM-Configura%C3%A7%C3%A3o-de-Integra%C3%A7%C3%A3o-Word-na-Oportunidade-Vendas-Int-Word
---

**Dúvida**

Como configuração a impressão da Proposta Comercial?   
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da release 12  
  
**Solução**

Para impressão da proposta seguir os procedimentos :

1. Parâmetros :

**1.1. MV\_PATWORD**: Com o caminho onde estão os DOTS na máquina do usuário CLIENT. Registrar um endereço que seja comum em todas as Estações de Trabalho (igual ao Servidor).  
Ou seja, todas as Estações de Trabalho devem possuir essa pasta dentro da C: e devem conter os registros .dot nesta pasta  
Exemplo: **c:\wordstd\**

**1.2. MV\_PATTERM**: O caminho em que será gravado o documento final impresso (arquivo do WORD).

É necessário que crie uma pasta dentro do diretório Wordtmp  
Crie a pasta "Propostas" por exemplo, e registre o caminho no parâmetro MV\_PATTERM. Registrar um endereço que seja comum em todas as Estações de Trabalho (igual ao Servidor).  
Ou seja, todas as Estações de Trabalho devem possuir essa pasta dentro da C:  
Exemplo: **c:\wordtmp\propostas\**

**1.3. MV\_DOCAR:** Caminho onde estão os DOTS originais SERVER.

**1.4. MV\_NOMEDOT**: Nome do arquivo que contém as macros usados na impressão. Nesse parâmetro deve conter o nome do arquivo .dot como por exemplo, o nome [MACROPADRAO.dot](http://macropadrao.dot/) (que são os arquivos disponível para baixar no inicio desta FAQ, na aba "Complementar - Download dos arquivos").  
  
Obs: No cadastro de Componente FATA630 (veja a seguir) terá que conter o mesmo nome, para referência do arquivo.  
  
Exemplo: **CRM-Exec\_Macro.dot**

**2. CADASTRO DOS COMPONENTES (FATA630)**

É necessário realizar o cadastro de cada uma das páginas de impressão (Componentes), do Modelo que deseja imprimir, através da rotina "Componentes de Impressão" (FATA630).

![impressao_proposta.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4408149067159)

**Documentação com a configuração completa em: <https://tdn.totvs.com/x/gmM-Dg>**

**IMPORTANTE!**

A partir da versão 12.1.2410, a utilização de SmartClient Remote (Desktop) ou WebApp, não afeta o funcionamento da integração e geração de arquivos de propostas comerciais via documento Word (Arquivos .dot).   
  
Ou seja, seu funcionamento continua valendo independente do formato de acesso feito.  
Para os acessos via SmartClient (WebApp), se faz necessário a configuração do WebAgent ([2. WebApp - WebAgent](https://tdn.totvs.com/pages/viewpage.action?pageId=655645934)) para que tenha o pleno funcionamento. Caso contrário, a leitura dos arquivos .dot não terá o seu funcionamento correto.
