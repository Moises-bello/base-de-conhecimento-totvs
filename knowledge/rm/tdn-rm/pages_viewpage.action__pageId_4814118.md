---
content_hash: c90407dd5d669fa8bb71f4d5b4afa018f3e355664e84fb6a73c839e77e8733e8
fetched_at: '2026-06-29T00:10:19.463861+00:00'
page_id: '4814118'
product: rm
source: tdn-rm
title: Cadastro e Envio do Conhecimento de Transporte Eletrônico CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4814118
version: 15
---

BLOCK

Cadastro e Envio do Conhecimento de Transporte Eletrônico CT-e

FAQ: **Cadastro e Envio do Conhecimento de Transporte Eletrônico (CT-e)**

***Como Fazer***

Como parametrizar o sistema para utilizar Conhecimento de Transporte Eletrônico em Movimentações de Saída?

***Definição do Processo***

Da mesma forma que a Nota Fiscal eletrônica (NF-e), o Conhecimento de Transporte Eletrônico (CT-e), tem como o objetivo principal a implantação de um modelo nacional de documento fiscal eletrônico com o intuito de substituir a emissão do documento fiscal (CTRC) em papel, simplificando assim o cumprimento das obrigações acessórias dos contribuintes e permitindo um melhor gerenciamento operações comerciais pelo Fisco.

A validade jurídica do documento eletrônico de conhecimento de transporte é garantida pela assinatura digital do emissor (Empresa) e a Autorização de Uso fornecida pela administração tributária do domicílio do contribuinte.

O contribuinte que desejar emitir o Conhecimento de Transporte Eletrônico deve se cadastrar previamente junto a SEFAZ para receber um certificado digital e uma senha de acesso que viabilizará a troca de informações entre o emitente do CT-e e a SEFAZ.

Solução

***Parametrizações Necessárias***

Antes de começar a parametrizar o sistema e utilizar o Conhecimento de Transporte Eletrônico é necessário que a empresa tenha se cadastrado junto a SEFAZ e tenha em mãos o certificado digital e a senha de utilização expedida pela SEFAZ aos contribuintes cadastrados.

***Parametrização da Integração Fiscal para Emissão do CT-e***

Acessar | **Opções | Parâmetros | RM Nucleus |** **Integrações | Fiscal | Parâmetros por Filial,** selecionar a filial onde será utilizado o CT-e e informar os seguintes dados:

**Conexões NF-e**

- Versão do Layout de CT-e Utilizado: Preencher com a versão atual do layout utilizado pela SEFAZ

**Ambiente NF-e**

- Ambiente de envio: Para realizar os primeiros testes é recomendado que seja utilizado o ambiente de “Homologação” e posteriormente, quando o recurso for posto de fato em produção esse parâmetro deve ser alterado para “Produção”

**Certificação Digital 2/2**

- Tipo do Certificado Digital: Informar tipo do arquivo do Certificado Digital. Deve-se observar a extensão do arquivo do Certificado ( ex: \*.pfx, \*.p12 e etc) e selecionar o correspondente.

- Certificado Digital: Deve-se informar o caminho onde se encontra o arquivo com o Certificado Digital emitido pela SEFAZ para comunicação entre as partes.

- Senha da Private Key: Informar a senha expedida junto com o Certificado Digital.

***Parametrização do Movimento para Cadastro do CT-e***

Acessar | **Opções | Parâmetros | RM Nucleus |** e selecionar processo onde o tipo de movimento a ser utilizado para este fim foi configurado. A seguir editar o mesmo e informar:

**Etapa Fis – Dados**

- Usar CTRC: Emitir CT-e;

**Etapa Mov – Datas**

- Data Emissão: Edita;

**Etapa Mov – Transporte**

- Editar Quantidade: Marcar;

- Editar Via de Transporte: Marcar;

- Editar Espécie: Edita;

- Tipo de Frete | CIF/FOB: Marcar;

- Editar Dados do Calculo de Frete da Mercadoria: Marcar;

- Editar Dados da Placa do Veiculo: Marcar;

\*\*Opcionalmente outras parametrizações a respeito do transporte poderão ser utilizadas a gosto do usuário. Neste documento são apresentadas apenas as parametrizações essenciais para a utilização e envio do CT-e\*\*

**Etapa Fis – Natureza**

- Natureza | Edição: Edita |

- Seleção Automática da Natureza: Definir o tipo de seleção da natureza

\*\*Parametrização específica para geração de lançamentos fiscais\*

**Etapa Fis – Escrituração**

- Gerar Escrituração: Habilitar

- Tipo Documento Escrituração | Código Default: Informar tipo de documento que possua o \*Código do Modelo do Documento: 57\*

- Tipo do Lançamento Fiscal da Transferência: Saída

\*\*Parametrização específica para geração de lançamentos fiscais\*\*

**Etapa Fis – Tributação**

- Incluir e parametrizar os tributos de forma que atenda aos dados a serem apresentados no item ou movimento.

\*\*Parametrização específica para geração de lançamentos fiscais\*\*

***Descrição do Processo***

A movimentação de “Emissão do Conhecimento de Transporte Eletrônico” será feita como de costume, tendo como particularidade o preenchimento dos campos apresentados nas abas | **Transporte e CTRC** |, pois tais dados são consistidos na geração do arquivo XML de envio do CT-e.

**Aba Transporte | Identificação**

- Informar o tipo de frete pertinente à movimentação, para termos de CTRC/CT-e deverá ser do tipo FOB.

- Informar o tipo de serviço de transporte

- Informar os dados do volume da carga (quantidade, espécie, valor da mercadoria)

**Aba Transporte | Transportadora**

- O campo Via de Transporte corresponde ao modal a ser utilizado pelo CT-e e deve ser preenchido obrigatóriamente

- Informar os veículos que farão o transporte da carga.

**Aba CTRC | Coleta / Entrega**

- Esta aba deve ser preenchida quando houver dados de coleta e entrega da mercadoria, observando que, a informação preenchida nos campos **| Estado – Município |** de coleta e entrega vão interferir diretamente na seleção da natureza de operação (se utilizar), onde será obedecida a seguinte regra:

1ª Hierarquia: A seleção da natureza de operação será feita obedecendo UF da Coleta e UF da Entrega preenchidos na aba **| CTRC | Dados de Transporte | Local de Coleta |** se o Lançamento Fiscal estiver vinculado a um documento do tipo CTRC

Onde:

- Se a UF da Coleta = UF da Entrega: Utiliza Natureza Interna (5.XXX);

- Se a UF da Coleta <> UF da Entrega: Utiliza Natureza Interestadual (6.XXX);

2ª Hierarquia: A seleção da natureza de operação será feita obedecendo estado do Cli\for preenchida na aba **| Transporte | Cli\For Origem /Destino |** do movimento;

3ª Hierarquia: A seleção da natureza de operação será feita obedecendo estado do Cli\for preenchido na aba **| Identificação | Cliente \ Fornecedor |.**

**Aba CTRC | Outros Dados**

- Informar os dados da Composição do Frete.

**Aba | CTRC Saída**

- A associação entre as notas fiscais e o CT-e poderá ser feita de duas formas, informando os dados das notas fiscais de saída manualmente ou vinculando notas fiscais de outros tipos de movimentos através do ícone **| [![clip_image002](http://lh6.ggpht.com/_G7KXZLoZDsY/TWPzgxMXkcI/AAAAAAAAGoM/GYThJ1FLllM/clip_image002_thumb.jpg?imgmax=800 "clip_image002")](http://lh5.ggpht.com/_G7KXZLoZDsY/TWPzgXnY6pI/AAAAAAAAGoI/zEtNtSqouC0/s1600-h/clip_image002%5B3%5D.jpg) Associar Notas Fiscais |,** onde será aberta outra tela para que seja feito filtro das movimentações de nota fiscal que serão associadas ao CT-e.

**Aba | Relação Seguros**

- O cadastro dos seguros relacionados à carga transportada é obrigatório. Pelo menos um seguro deve ser incluído para o envio do CT-e

**Aba | Doc. Anteriores**

- O cadastro dos dados documentos anteriores é opcional no caso de CT-e normal ou Substituto. Porém se o tipo do serviço for de Redespacho ou Redespacho Intermediário, este(s) cadastro(s) será(ão) necessário(s) para o envio do CT-e.

**Aba | Motoristas**

- O cadastro dos dados do(s) motorista(s) é opcional e fica a cargo do usuário informá-los ou não..

**Permissão de Acesso no Perfil**

- O usuário deverá possuir as permissões do Menu utilitários:

Cadastros | Segurança | Perfis | Edita o Perfil desejado | Acesso a Menus | [09] Utilitários | [09.30] SPED | [09.30.04] CT-e

***Informações Adicionais***

- O sistema não faz validação entre o valor do movimento de CT-e com o valor das notas fiscais vinculadas ao mesmo.

***Envio do CT-e para a SEFAZ***

Após a inclusão do movimento de conhecimento de Transporte, é hora de enviá-lo a SEFAZ para que seja autorizado e então o DACTE (Documento Auxiliar de Conhecimento de Transporte Eletrônico) possa ser impresso e a carga possa seguir viagem.

Para isso é necessário acessar a tela de ‘Conhecimentos de Transporte Eletrônico’ em **| Utilitários | SPED | CT-e(Transporte)** e selecionar | **Processos | Enviar CT-e |.**

A tela de filtro será apresentada para que o usuário informe os dados necessários para filtrar os movimentos que se deseja enviar e clicar em | **Executar |.**

Após o envio, é gerado um registro de envio do CT-e com informações referentes ao mesmo com o Status “Pendente”.

**Importante!** O usuário deve aguardar alguns minutos para que os dados sejam aprovados pela SEFAZ,

Para consultar a aprovação do CT-e, o usuário poderá acessar o caminho **|** **Processos | Consultar Autorização/Cancelamento |.**

Caso os dados do CT-e enviado sejam aprovados, o usuário poderá imprimir o documento DACTE através do caminho **|** **Processos | Imprimir Relatório CT-e |.** Do contrário**,** o CT-e será rejeitado e o motivo será informado no log do processo e registrado no ‘Histórico de Conhecimento de Transporte(CT-e)’. Neste caso o usuário deverá acertar o movimento rejeitado para adequar a situação do CT-e.

Após acertar as inconsistências do CT-e no movimento, o usuário poderá reenviá-lo para a aprovação, selecionando o registro correspondente, com Status “Rejeitado” na tela de conhecimentos de transporte e executando novamente o processo **| Enviar CT-e |.**

***Informações Adicionais***

- Para enviar os dados através da rede até a SEFAZ é necessário ter instalado e configurado os aplicativos TOP Connect e TSS (TOTVS SPED Services). Para mais informações sobre a instalação e configuração destes, acesse:

<Link do TOP Connect e TSS >

<Link do TSS >

***Escrituração do Movimento de CTRC***

A escrituração dos movimentos será feita como de costume onde o usuário dever acessar **| Opções | Escrituração de Lançamentos – RMLIBER |** e fazer o filtro das movimentações de nota fiscal e escriturá-las. A seguir escriturar a nota de CT-e

Depois de concluído processo de escrituração, acessar o RMLIBER em **| Cadastro | Manutenção de Lançamentos de Saída |** e editar o lançamento fiscal de CTRC, serão apresentadas informações do conhecimento de transporte.

Na aba **| Dados do Transporte | CTRC | Notas Fiscais que Acobertam a Carga Transportada** serão apresentadas informações das notas fiscais vinculadas ao CTRC, ressaltando que a rotina de escrituração pertence ao aplicativo RM Liber.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Rpt/Rpt.Reports.aspx)

**COMUNIDADE **[R@Materiais e Finanças](https://totvs.byyou.com/?space=rmateriais)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015
