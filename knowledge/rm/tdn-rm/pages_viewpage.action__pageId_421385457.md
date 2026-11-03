---
content_hash: bf2aafd23c8c170563e2e124dd74154146ebd65df33d49ce009bc89df5f8334e
fetched_at: '2026-06-29T00:09:16.111450+00:00'
page_id: '421385457'
product: rm
source: tdn-rm
title: Importação de Insumos/Composições/Tarefas via Arquivo Texto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385457
version: 3
---

---

A importação de arquivos texto consiste em incluir insumos/composições/tarefas em um novo projeto ou em um projeto já existente. Está opção somente ficará habilitada caso algum projeto esteja aberto e o usuário tenha permissão. A funcionalidade consiste em gerar uma planilha ou cenário espelho do arquivo texto que se escolhida para importação.

**Passo a passo:** Defina qual o tipo de importação: Insumos, Composições ou Tarefas. **Caso Insumo:** 1. Arquivo (Localização + Nome): Informe a localização e o nome do arquivo a ser importado; 2. Defina se os preços importados serão ativados através da opção Ativar Preços Importados; 3. Importe o arquivo;

**Observação:** Caso algum insumo importado não tenha descrição para o preço será adotada a seguinte descrição Preço em DD/MM/AAAA, onde DD/MM/AAAA é a data do dia da importação; O código do insumo respeitará  a máscara definida no projeto, sendo que quando algum caracter não corresponda à máscara, será aberta uma tela solicitando que o mesmo seja alterado por um código válido.  
 O layout utilizado deve conter os campos abaixo, sendo que alguns não são obrigatórios:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Campo | Tamanho | De | Até | Obrigatório | Observação |
| Status | 1 | 001 | 001 | S | Identificado com um \* (asterisco). |
| Código | 20 | 002 | 021 | S |  |
| Descrição | 130 | 022 | 151 | S |  |
| Unidade | 10 | 152 | 161 | S |  |
| Grupo de Custo | 20 | 162 | 181 | S |  |
| Grupo DNIT | 1 | 182 | 182 | N |  |
| Preço Unitário | 15 | 183 | 197 | N | Separa casas decimais por ponto. |
| Preço Improdutivo | 15 | 198 | 212 | N | Separa casas decimais por ponto. |
| Data Preço | 8 | 213 | 220 | N | Formato: DD/MM/AAAA |
| Moeda Preço | 10 | 221 | 230 | N |  |
| Descrição Preço | 30 | 231 | 260 | N | Valores válidos: Fracionado:s, sim, o Não Fracionados>n,não,1 |
| Fracionamento | 3 | 261 | 263 | N |  |

**Caso Composições:**

1. Arquivo (Localização + Nome): Informe a localização e o nome do arquivo a ser importado;

2. Importe o arquivo;

**Observação:** Essa importação também poderá ser utilizada para importar somente recursos, pois, caso já exista no sistema uma composição que também está no arquivo texto, o sistema importará somente os recursos diferente dos já existentes, ou seja, adiciona somente os novos recursos. Caso o recurso não puder ser fracionado, a quantidade será arredondada para cima.

Há três tipos de arquivos para importação de Composições:

O primeiro importa o cabeçalho da composição:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Campo | Tamanho | De | Até | Obrigatório | Observação |
| Status | 1 | 001 | 001 | S | Identificado por \* (asterisco) |
| Código | 20 | 002 | 021 | S |  |
| Descrição | 200 | 022 | 221 | S |  |
| Unidade | 10 | 222 | 231 | S |  |
| Produção | 15 | 232 | 246 | N | Separas casas decimais por ponto |

O segundo importa os recursos que são insumos (I):  
  

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Campo | Tamanho | De | Até | Obrigatório | Observação |
| Códido da Composição | 20 | 002 | 002 | S |  |
| Código do Insumo | 20 | 022 | 041 | S |  |
| Quantidade | 15 | 042 | 056 | S | Separar casas decimais por ponto |
| Coef. Produtivo | 15 | 157 | 071 | N | Separar casas decimais por ponto |
| DMR | 15 | 072 | 086 | N | Separar casas decimais por ponto |
| Origem Recurso | 1 | 087 | 087 | N | Global: G  e g; Local: demais valores |

   
  E o terceiro importa os recursos que são composições auxiliares:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Campo | Tamanho | De | Até | Obrigatório | Observação |
| Código da Composição | 20 | 002 | 021 | S |  |
| Códico da Composução Auxiliar | 20 | 022 | 041 | S |  |
| Quantidade | 15 | 042 | 056 | S | Separar casas decimais por ponto. |
| Coeficiente Produtivo | 15 | 0157 | 071 | N | Separar casas decimais por ponto. |
| DMT | 15 | 0172 | 086 | N | Separar casas decimais por ponto. |
| Grupo DNIT | 1 | 087 | 087 | N |  |
| Origem do Recurso | 1 | 088 | 088 | N | Globais: G e g; Locais: demais valores |

**Atenção:**   
 Caso a composição auxiliar for do tipo por produção o Grupo DNIT é obrigatório.   
 **Caso Tarefas:**  
 1. Arquivo (Localização + Nome): Informe a localização e o nome do arquivo a ser importado; 2. Defina qual para cenário as tarefas serão importadas; 3. Código a ser acrescentado no início do Código da Tarefa (opcional); 4. Defina o tamanho do código da tarefa; 5. Importe o arquivo;  
 **Observação:** Antes da importação, verifique nos parâmetros do projeto se a máscara definida para as tarefas corresponde à máscara definida no arquivo a ser importado;

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Campo | Tamanho | De | Até | Obrigatório | Observação |
| Código | 20 ou 60 | 1 | 20 ou 60 | S | Com máscara |
| Nome | 90 | 21 | 110 | S |  |
| Quantidade | 15 | 111 | 125 | S |  |
| Valor Cotado | 15 | 126 | 140 | N |  |
| Unidade | 10 | 141 | 150 | S | Com máscara |
| Recurso | 20 | 151 | 170 | N |  |
| BDI | 15 | 171 | 185 | N |  |
| Descrição | 250 | 186 | 435 | N |  |

  Veja Também

---
