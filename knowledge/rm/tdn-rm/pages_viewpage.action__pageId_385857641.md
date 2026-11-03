---
content_hash: 24f2f746ff5d266aecadeb1fe267d42567649f5877182f1ca2f608e3cb85c038
fetched_at: '2026-06-29T00:09:07.915944+00:00'
page_id: '385857641'
product: rm
source: tdn-rm
title: RMPAT00003_Importação de Titulo Gestão Patrimonial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=385857641
version: 5
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Gestão Patrimonial |
| **Versões:** | 12.1.19 |
| **Ocorrência:** | Importação de Titulos via Conceito. |
| **Ambiente:** |  |
| **Passo a passo:** | Para realizar a importação de dados por arquivo texto no TOTVS Gestão Patrimonial, será utilizada a ferramenta "RM Conector", que facilita a execução destas operações de forma dinâmica, utilizando a própria regra dos cadastros.   Embora a operação seja simples, alguns cuidados devem ser tomados antes de realizá-la, certificando-se que os dados a serem importados estão corretos, evitando assim, erros durante processo de importação de dados.    **DESENVOLVIMENTO/PROCEDIMENTO** Para o processo de importação via conceito, deve ser criado um Arquivo Texto, conforme Layout disponibilizado:  [Layout de Importação de Títulos](https://tdn.totvs.com/pages/releaseview.action?pageId=423938324).  Para realizar o processo de importação via Conceito, deve-se:  a) Acessar a Nova MDI / menu principal / Integrações / Conceito.      Execute o processo de importação do conceito (CONPAT0048) disponível em > processos > importar conceito.        b) Edite o conceito importado, acesse a guia 'Conexões Origem' e informe o caminho correspondente, onde o Arquivo Texto se encontra. Exemplo:  C:\documentos\importação\arquivo de importação      c) Após informar o caminho do Arquivo Texto - com as informações a serem importadas – acesse o menu 'Processos' / 'Processar Conceito'      Após a execução do processo, verifique o Log apresentado.    **ARQUIVO TEXTO**   * Deve ser usado ponto e vírgula ( ; ) como separador lógico; * Deixe espaços em branco, quando não utilizar determinado campo que não é obrigatório. * Segue abaixo EXEMPLO do Arquivo txt. para importação:   16;1;1;TOTVS 16.01;1;1;TOTVRES    **INFORMAÇÕES ADICIONAIS**  Após realizar a importação, é importante conferir se os dados foram importados corretamente;   Os arquivos padrões do Conceito estão disponibilizado no seguinte diretório: C:\totvs\CorporeRM\ObjetosGerenciais\Conceito \CONPAT0045 - Importação Patrimônio.icp;   Caso algum item do arquivo de origem não atenda as validações do conceito criado, nenhum registro será importado |
| **Observações:** |  |
