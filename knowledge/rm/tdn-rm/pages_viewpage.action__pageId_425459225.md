---
content_hash: da7c56717d6fcca7c7ab29f6fec1e6eaa076b067fe6e9106c9c4030b6efaa341
fetched_at: '2026-06-29T00:09:34.701926+00:00'
page_id: '425459225'
product: rm
source: tdn-rm
title: Importação de dados.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459225
version: 12
---

Neste processo é possível importar dados de outros sistemas para o TOTVS Gestão Bibliotecária através de um arquivo txt. Estes arquivos são gerados com base em um layout previamente definido. Os dados que podem ser importados através deste processo são: Áreas e Subárea de conhecimento, Assuntos, Autores, CUTTER/PHA, Editoras, Exemplares, Publicações e Usuários.

**Importante:**

**1)** O formato dos arquivos é TXT com duas opções de separação entre os campos, dependendo da configuração do processo:  - por ";" (ponto-e-vírgula). Ex: 147;Biblioteca  - por "@;" (arroba e ponto-e-vírgula). Ex: [147@;Biblioteca](mailto:147@;Biblioteca)

**2)** Para campos numéricos os zeros à esquerda (antes da vírgula) e à direita (depois da vírgula) são desnecessários.

**3)** Os registros devem estar em uma única linha e, caso não existir valor para um campo, pode deixar em branco, sem apagar o separador.

**4)** As tabelas abaixo devem ser cadastradas antes da importação das tabelas descritas neste documento, pois delas dependem estas importações.

**5)**As posições que forem de preenchimento **OBRIGATÓRIO** devem ser preenchidas e não podem ficar em branco.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **REFERÊNCIA** | **TABELA** | **SISTEMA** | **DESCRIÇÃO** | **ITEM DE MENU** |
| 1 | LPAIS | TOTVS Gestão Bibliotecária | Países | Tabelas auxiliares → Países |
| 2 | LPUBLIC | TOTVS Gestão Bibliotecária | Publicações | Acervo → Publicações |
| 3 | TUND | TOTVS Gestão de Estoque, Compras e Faturamento | Unidades de medida | Cadastros → Mais... → Tabelas auxiliares → Unidade |
| 4 | LGRUPOPUBLIC | TOTVS Gestão Bibliotecária | Grupos de publicação | Tabelas auxiliares → Grupos de publicação |
| 5 | LLOCALPUB | TOTVS Gestão Bibliotecária | Locais de publicação | Tabelas auxiliares → Locais de publicações |
| 6 | LPERIODICIDADE | TOTVS Gestão Bibliotecária | Periodicidades | Tabelas auxiliares → Periodicidades |
| 7 | LTIPOUSUARIO | TOTVS Gestão Bibliotecária | Tipos de usuário | Cadastros → Usuários → Tipos de usuários |
| 8 | PCODNACAO | TOTVS Folha de Pagamento | Nacionalidades | eSocial → Endereços → Classificação de nações |
| 9 | GETD | TOTVS Gestão Fiscal | Estados da federação | Cadastros → Globais → Mais... → Estados |

Abaixo o layout dos arquivos:

Aviso

Para considerar corretamente acentos e caracteres especiais na importação o arquivo TXT deve estar na codificação ANSI.
