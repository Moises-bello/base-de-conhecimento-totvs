---
article_id: 360025147611
category: Configurador
content_hash: f2016604630f91ef35907b95abde8212ffde8c948a2bf27fa45a1badffbc706b
fetched_at: '2026-06-28T22:42:19.009810+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Criação de Empresas e Filiais
type: support-article
updated_at: '2026-05-08T13:02:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025147611-Framework-Linha-Protheus-Cria%C3%A7%C3%A3o-de-Empresas-e-Filiais
---

**Dúvida:**  
 Como fazer para criar empresas e filiais no Protheus?  
   
 **Ambiente:**  
 Protheus – Configurador – A partir da versão 11  
   
 **Solução:**A partir da versão 11 do Protheus, existem 2 maneiras de criar uma estrutura de empresas:  
  
1. Conceito Empresa / Filial  
2. Conceito de Gestão de Empresas  
  
O novo conceito de **Gestão de Empresas** tem por finalidade:  
  
- Possibilitar o compartilhamento do Dicionário de Dados de várias empresas pelo Microsiga Protheus  
- Introduzir Unidade de Negócios  
- Permitir a configuração do tamanho do código de Empresa e Filial  
- Permitir a configuração do compartilhamento entre Empresas, Unidades de Negocio e Filiais

|  |
| --- |
| Importante:  A partir da LIB liberada em agosto de 2014, o Protheus não considera mais o campo M0\_DTVLD (data de validade) no arquivo de empresas sigamat.emp.  Da mesma forma, lançamentos futuros em rotinas dos módulos, como Financeiro e Contábil, por exemplo, não consideram esse campo para permitir ou não o lançamento na data futura.  Então, se você tem em seu ambiente LIB com data igual ou superior a esta, não precisa mais revalidar o sigamat.emp nos seguintes casos: - vencimento do sigamat.emp (ele não terá mais data de vencimento) - criação de nova empresa/filial (a menos que o contrato seja Corporativo¹) - alteração de campos obrigatórios do cadastro de filial pelo Configurador  ¹ para clientes com contrato Corporativo, ainda é necessário revalidar o sigamat.emp quando incluir uma nova Empresa ou Filial, devido ao fato que para este tipo de contrato, o CNPJ é verificado no sigamat.emp e no arquivo de licenças.  Caso a LIB seja anterior, é necessário abrir um chamado para o CST-Senhas (ou utilizar o Autoatendimento CST no Portal), enviando o arquivo sigamat.emp atual para revalidação. |

|  |
| --- |
| Importante: Grupos de Empresas com código maior que 2 dígitos já é considerado como modelo de Gestão de Empresas. |

Abaixo iremos detalhar a criação de empresas / filiais nos dois conceitos.

**1. Conceito Empresa / Filial**  
Permite a criação da empresa, e de filiais abaixo dela. Há a possibilidade de compartilhamento de tabelas entre as filiais. É um conceito mais "simples".  
  
Para criar empresa/filial utilizando este conceito:  
1. Acesse o Configurador > Ambiente > Empresas > **Grupo de Empresas**  
2. Clique em **Incluir**  
3. Em **Código**, selecione um código que definirá essa empresa (Ex.: 01)  
4. Em **Descrição**, defina o nome da empresa  
5. Em **Tamanho**, defina a quantidade de caracteres que o campo Filial das tabelas irá ter (Ex.: 2)  
6. Em **Leiaute**, defina como serão compostos os caracteres para formar o código da filial. Se o Tamanho for igual a 2, conforme exemplo, o Leiaute poderia ser FF, indicando que o código da filial será composto por 2 caracteres representando o código da filial (F=Filial).  
  
Conforme o Leiaute criado, na parte logo abaixo na tela, aparecerá a Sequência, Sigla, Ordem e Máscara para cada dígito. Para cada identificador será permitido (não obrigatório) definir uma máscara de restrição para preenchimento conforme o exemplo a seguir:  
  
F - 0-2 (Somente números entre 0 e 2)  
F - 5-9 (Somente números entre 5 e 9)  
\* Para maiores informações sobre as máscaras possíveis, clique 2 vezes no campo da coluna Máscara e pressione F1  
  
![Picture_2017-01-19_18_25_27.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023500652)  
  
7. Após terminar a configuração da empresa, clique em **Confirmar**. Será exibida uma janela perguntando se **Deseja criar o dicionário de dados agora?**  
  
![Picture_2017-01-19_16_56_26.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023537971)

Se clicar em Não, o dicionário será criado ao acessar algum módulo por esta empresa. Se clicar em Sim, será feita uma nova pergunta:

**Criar Dicionário:**  
**. a partir de uma base existente:** os arquivos de dicionário desta empresa serão criados a partir do dicionário de outra empresa já existente, mantendo dessa forma os mesmos campos, tabelas, etc, criados na empresa original  
**. com registros padrao:** os arquivos de dicionário desta empresa serão criados a partir do dicionário padrão do Protheus  
**. nao criar agora:** o dicionário será criado ao acessar algum módulo por esta empresa

![Picture_2017-01-19_17_07_08.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023502992)  
  
Se for selecionada a opção **a partir de uma base existente**, será aberta uma janela para selecionar qual a empresa base, e em seguida, uma janela questionando sobre o **Diretório dos arquivos de dados**. Selecione a pasta **data**.  
  
![Picture_2017-01-19_17_21_27.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023538351)

Se for selecionada a opção "**com registros padrao**", será aberta uma janela solicitando informar o País. Tenha certeza de estar selecionado o país correto antes de continuar. Em seguida, será exibida uma janela questionando sobre o **Diretório dos arquivos de dados**. Selecione a pasta **data**.

Ao finalizar, saia do menu Grupo de Empresas, e acesse o menu **Filial**.  
1. Acesse o Configurador > Ambiente > Empresas > **Filial**  
2. Clique em **Incluir**  
3. Em **Grupo**, digite o código do Grupo de Empresas que criou, o Grupo de Empresas a que esta Filial fará parte (Ex.: 01)  
4. Em **Código**, insira o código que esta Filial terá (segundo a máscara criada no exemplo, a filial deverá ter 2 dígitos, sendo o primeiro um número entre 0 e 2, e o segundo um número entre 5 e 9. Ex.: 17)  
5. Em **Descrição**, defina o nome da Filial  
6. Os outros campos, que não tem asterisco, são de preenchimento opcional  
7. Após terminar, clique em **Confirmar**  
8. A empresa e filial estão prontas para uso

**2. Conceito de Gestão de Empresas**  
Este conceito permite uma configuração mais abrangente, pois aumenta as divisões de empresas em unidades de negócios e filiais, permite também maior escalabilidade de compartilhamentos. Abaixo as definições de cada parte da estrutura de Gestão de Empresas:

**- Grupo de Empresas**  
Conjunto de empresas que estão ligadas entre si por razões diversas e que compartilham as mesmas definições do modelo de dados.

**- Empresas**  
Conjunto de Filiais ou Unidades de Negócios que estão dentro da mesma dependência jurídica ou fiscal.

**- Unidade de Negócios**  
Conjunto de filiais que estão dentro da mesma atividade econômica.

**- Filial**  
Estabelecimento empresarial dependente de outro que pratica atos que têm validade jurídica ou fiscal.

Para a criação de empresa/filial seguindo o conceito de Gestão de Empresas, siga os passos abaixo:

1. Acesse o Configurador > Ambiente > Empresas > **Grupo de Empresas**  
2. Clique em **Incluir**  
3. Em **Código**, selecione um código que definirá essa empresa (Ex.: 12)  
4. Em **Descrição**, defina o nome da empresa  
5. Em **Tamanho**, defina a quantidade de caracteres que o campo Filial das tabelas irá ter (Ex.: 6)  
6. Em **Leiaute**, defina como serão compostos os caracteres para formar o código da filial. Se o Tamanho for igual a 6, conforme exemplo, o Leiaute poderia ser EEUUFF, indicando que o código da filial será composto por 2 caracteres representando o código da empresa, 2 caracteres representando o código da unidade de negócios e 2 caracteres representando o código da filial (E=Empresa / U=Unidade de Negócios / F=Filial)

Conforme o Leiaute criado, na parte logo abaixo na tela, aparecerá a Sequência, Sigla, Ordem e Máscara para cada dígito. Para cada identificador será permitido (não obrigatório) definir uma máscara de restrição para preenchimento conforme o exemplo a seguir:

E - 0-9 (Somente números entre 0 e 9)  
E - 5-9 (Somente números entre 5 e 9)  
U - A-Z (Somente caracteres entre A e Z)  
U - X-Z (Somente caracteres entre X e Z)  
F - !-! (Qualquer dígito numérico ou alfanumérico)  
F - A,B,5,9 (Somente caracteres entre A,B,5 e 9)  
F - 0-9 (Somente números entre 0 e 9)  
F - A-Z (Somente caracteres entre A e Z)  
\* Para maiores informações sobre as máscaras possíveis, clique 2 vezes no campo da coluna Máscara e pressione F1

![Picture_2017-01-19_18_40_15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023541631)  
  
7. Após terminar a configuração da empresa, clique em Confirmar. Será exibida uma janela perguntando se **Deseja criar o dicionário de dados agora?**.  
  
![Picture_2017-01-19_16_56_26.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023537971)

Se clicar em Não, o dicionário será criado ao acessar algum módulo por esta empresa. Se clicar em Sim, será feita uma nova pergunta:

**Criar Dicionário:**  
**. a partir de uma base existente:** os arquivos de dicionário desta empresa serão criados a partir do dicionário de outra empresa já existente, mantendo dessa forma os mesmos campos, tabelas, etc, criados na empresa original  
**. com registros padrao:** os arquivos de dicionário desta empresa serão criados a partir do dicionário padrão do Protheus  
**. nao criar agora:** o dicionário será criado ao acessar algum módulo por esta empresa

![Picture_2017-01-19_17_07_08.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023502992)

Se for selecionada a opção **a partir de uma base existente**, será aberta uma janela para selecionar qual a empresa base, e em seguida, uma janela questionando sobre o **Diretório dos arquivos de dados**. Selecione a pasta **data**.

Se for selecionada a opção "**com registros padrao**", será aberta uma janela solicitando informar o País. Tenha certeza de estar selecionado o país correto antes de continuar. Em seguida, será exibida uma janela questionando sobre o **diretório dos arquivos de dados**. Selecione a pasta **data**.

Ao finalizar, saia do menu Grupo de Empresas, e acesse o menu **Empresas**.

1. Acesse o Configurador > Ambiente > Empresas > **Empresas**  
2. Clique em **Incluir**  
3. Em **Grupo**, digite o código do Grupo de Empresas que criou, o Grupo de Empresas a que esta Empresa fará parte (Ex.: 12)  
4. Em **Código**, insira o código que esta Empresa terá (Ex.: 01)  
5. Em **Descrição**, defina o nome da Empresa  
6. Clique em **Confirmar**

Ao finalizar, saia do menu Empresas, e acesse o menu **Unidade de Negócios**.  
1. Acesse o Configurador > Ambiente > Empresas > **Unidade de Negócios**  
2. Clique em **Incluir**  
3. Em **Grupo**, digite o código do Grupo de Empresas que criou, o Grupo de Empresas a que esta Empresa fará parte (Ex.: 12)  
4. Em **Empresa**, digite o código da Empresa que criou (Ex.: 01)  
5. Em **Código**, insira o código que esta Unidade de Negócios terá (Ex.: 01)  
6. Em **Descrição**, defina o nome da Unidade de Negócios  
7. Clique em **Confirmar**

Ao finalizar, saia do menu Unidade de Negócios, e acesse o menu **Filial**.  
1. Acesse o Configurador > Ambiente > Empresas > **Filial**  
2. Clique em **Incluir**  
3. Selecione o código do Grupo, Empresa e Unidade de Negócios a que essa Filial pertence, então defina um código para esta Filial (Ex.: 01)  
4. Em **Descrição**, defina o nome da Filial  
5. Os outros campos, que não tem asterisco, são de preenchimento opcional  
6. Após terminar, clique em **Confirmar**  
7. A empresa e filial no modo Gestão de Empresas estão prontas para uso
