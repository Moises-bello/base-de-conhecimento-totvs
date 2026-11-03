---
content_hash: 2d708d19d9a554e76a3cc216124720a7d889872db6c6748aedc9f31635babd89
fetched_at: '2026-06-29T00:08:52.735611+00:00'
page_id: '342303935'
product: rm
source: tdn-rm
title: RMPAT00002_Importação Patrimonial Via Conceito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=342303935
version: 10
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Gestão Patrimonial |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Importação Patrimonial via Conceito. |
| **Ambiente:** |  |
| **Passo a passo:** | Para realizar a importação de dados por arquivo texto no TOTVS Gestão Patrimonial, será utilizada a ferramenta "RM Conector", que facilita a execução destas operações de forma dinâmica, utilizando a própria regra dos cadastros.  Embora a operação seja simples, alguns cuidados devem ser tomados antes de realizá-la, certificando-se que os dados a serem importados estão corretos, evitando assim, erros durante processo de importação de dados.  **DESENVOLVIMENTO/PROCEDIMENTO**  Para o processo de importação via conceito, deve ser criado um Arquivo Texto, conforme Layout disponível em   Para realizar o processo de importação via Conceito, deve-se:  a) Acessar a Nova MDI / menu principal / Integrações / Conceito     b) Clique processos > importar conceito >clique em ( ... ) > acesse o caminho   C:\TOTVS\CorporeRM\ObjetosGerenciais\Conceito selecione o conceito  CONPAT0045 - Importação Patrimônio.concept  Observação: desmarque a opção de substituir existente.  c) Após importar o conceito > selecione edita o conceito > clique em arquivo > editar > na opção arquivo clique nos três pontinho ( ... ) selecione a opção de arquivo fixo > e informa o arquivo texto > clique em ok.    Após selecione o conceito > processo > processar novo conceito.      **ARQUIVO TEXTO**   * Deve ser usado ponto e vírgula ( ; ) como separador lógico; * Deixe espaços em branco, quando não utilizar determinado campo que não é obrigatório. * Segue abaixo EXEMPLO do Arquivo txt. para importação:   01.01.900;01;0;1;TESTE TESTE TESTE;0;01/04/2012;100,00;;000001;;;;;00011;;;;1;02.1.1.3;;;;;0;;10,00;N;    **INFORMAÇÕES ADICIONAIS**  Após realizar a importação, é importante conferir se os dados foram importados corretamente;    Os arquivos padrões do Conceito estão disponibilizado no seguinte diretório: C:\totvs\CorporeRM\ObjetosGerenciais\Conceito \  Após carregar o arquivo, que contêm a parametrização da importação desejada, o cadastro do Conceito será preenchido automaticamente, necessitando assim, que o usuário apenas altere o caminho de origem do arquivo.  Caso algum item do arquivo de origem não atenda as validações do conceito criado, nenhum registro será importado.  Após realizar o processo, e necessário realizar o processo de cálculo de patrimônio, em cadastro > cálculo > selecione o cálculo em questão > processo > cálculo do patrimônio. |
| **Observações:** | Observação: O campo 26 e responsável pela depreciação acumulada corrigida, este cálculo deve ser informado manualmente, e deve ser informado, de sua data de aquisição até um mês antes de sua competência atual, pois a cálculo da competência atual o sistema calcula automaticamente.  Fonte: |
