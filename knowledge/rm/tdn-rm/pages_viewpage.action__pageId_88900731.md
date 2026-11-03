---
content_hash: 61b501423d9816c26332ef187446c85ade7a1dfe4d7855fb26fb54d854864df8
fetched_at: '2026-06-29T00:12:01.169615+00:00'
page_id: '88900731'
product: rm
source: tdn-rm
title: Geração da Rotina FCI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=88900731
version: 9
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** 11.52.58 |
| **Processo** | **:** | FCI |
| **Subprocesso** | **:** | Geração da Rotina FCI |
| **Data da publicação** | **:** | 17/10/2013 |

**1. Passos para implantação do processo da Rotina FCI – Ficha de Conteúdo de Importação**

Recomendamos que esse procedimento seja feito numa base teste (backup da oficial) e somente após a validação na base oficial:

1- Rodar o script   
 2- Atualizar a versão da Biblioteca 11.52.58.xxx e superiores   
 3- Versão do Aplicativo Totvs Gestão Fiscal 11.52.58.xx e superiores.   
 4- Importar o Leiaute da Rotina.   
 5- Realizar o cálculo Automaticamente no Cadastro do Produto|Processos Cálculo Conteúdo de Importação (Veja o COMO FAZER- Cálculo VI e VO)  
 6- Gerar a Rotina FCI.  
 7- Validar os valores gerados.

**2. Processos**

Contribuintes de ICMS de todo o país devem encaminhar as Fichas de Conteúdo de Importação - FCI para o endereço [www.fazenda.sp.gov.br/fci](http://www.fazenda.sp.gov.br/fci). neste site também esta disponível *O Manual do Usuário* que ilustra os procedimentos necessários para o preenchimento, transmissão e obtenção dos Números de Controle da FCI.

Para geração da Rotina será selecionado os produtos que foram submetidos ao Cálculo do Conteúdo de Importação e que não tenha Número de FCI gerado.

Considerações para geração do arquivo *Texto* da Rotina :

* Selecionamos os produtos pelo o qual o Cálculo do Conteúdo de Importação já tenha sido executado e que o Campo Número de FCI esteja em branco.

* Conteúdo de Importação <=40%, somente será considerado na geração do Arquivo texto da Rotina se o parâmetro na tela de geração da Rotina esta habilitado. Caso contrario será gravado no Cadastro do Produto|Anexo|FCI, o Cálculo do Conteúdo de Importação, mas não será selecionado para geração do Arquivo texto.

* Conteúdo de Importação >40% e <=70%, sempre será selecionado na geração do Arquivo Texto da Rotina;

* Conteúdo de Importação >70, sempre será selecionado na geração do Arquivo Texto da Rotina;

* Conforme a Legislação um novo Número de FCI somente deve ser gerado se houver alteração de Faixa no Cálculo do Conteúdo de Importação.

* Sempre que for feito o recalculo e não houver alteração da Faixa vamos gravar o Cálculo atual, copiando o Número do FCI gravado no cálculo anterior;

* Quando houver alteração de Faixa o produto será selecionado na geração do Arquivo Texto da Rotina.

**Observação:** Não será mais necessário fazer a parametrização dos Produtos no Parâmetros |Processo| FCI.

**3. Geração da Rotina**

Acesse o menu Rotina Legais|Rotinas Federais|FCI – Ficha de Conteúdo de importação

**Opção de Exportação:** Nesta opção será gerada o arquivo Texto para ser importado\Validado no programa  da SEFAZ (FCI)

**Coligada:** Informar a coligada para a qual deseja gerar a Rotina

**Filial:** Informar a Filial

**Versão:** Versão de leiaute do arquivo, informação disponível no manual do usuário que a SEFAZ disponibiliza.

**Personalizar Código do Produto:** Selecionar qual o Código do produto será utilizado na geração do arquivo\Opções Código - Identificador(IDPRD) – Código Reduzido – Código Auxiliar todos estes campos estão disponível no Cadastro do Produto.

**Selecionar Produtos com Conteúdo de Importação Menor ou Igual a 40%:** Com este ícone habilitado ao gerar a Rotina será selecionado o Produto que tem o Conteúdo de Importação <=40%.   
 Após preencher as informações necessárias para gerar a Rotina – Clicar em Avança e Executar. Após gerar aparece a tela abaixo, deve ser verificado se ocorreu erro em algum Registro ou Processo.

**Opção de Importação:** Nesta opção é possível importar o arquivo texto de retorno enviado pela SEFAZ (efetuar UPLOAD) com os números das FCI's geradas pela SEFAZ. Fazendo isto os Números da FCI dos produtos constantes no arquivo serão gravados no Cadastro do Produto\Anexo FCI's do Produto\Campo Número FCI.

Após a importação é apresentada a tela Processo Concluído com Sucesso ou alguma mensagem de erro de Leiaute.

**4. Informações no Campo Dados Adicionais da NFe**

Será gerado com o Número da FCI informada no Cadastro do Produto|Anexos FCI – Número FCI, conforme a seguinte regra:

* CFOP iniciadas com 6
* Origem da Mercadoria (Procedência)

3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% (quarenta por cento) e inferior ou igual a 70% (setenta por cento);  
 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40% (quarenta por cento);  
 8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% (setenta por cento).

* Será selecionado o Número da ultima FCI cadastra para o produto na filial e coligada que o processo estive sendo executado.

**Para maiores informações:**

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/RequisitosFCI.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
