---
content_hash: d66638199449729ba03ed3350b7abf381e9b6b39f474f9b074982a2125325af5
fetched_at: '2026-06-29T00:09:34.772216+00:00'
page_id: '425459246'
product: rm
source: tdn-rm
title: Layout de Importação de Publicações 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459246
version: 9
---

1619547002461\_-1593961755

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **ORDEM** | **NOME** | **DESCRIÇÃO** | **OBRIGATÓRIO** | **TIPO** | **VALIDAÇÃO/MÁSCARA** |
| 1 | CODPUBLIC | Código da publicação | Não | Inteiro |  |
| 2 | TITULO | Título principal da publicação | Sim | Texto(200) |  |
| 3 | TIPOPUBLIC | Tipo de publicação | Sim | Inteiro | 1 - Livro 2 - CD-ROM 3 - Disquete 4 - Periódico 5 - Slide 6 - Fita de vídeo 7 - Tese 8 - Fita cassete 9 - DVD 10 - Documento 11 - Monografia/Dissertação/Tese 12 - Dissertação 13 - Arquivo Digital 14 - Material 15 - Fotografia 16 - Analítica de livro 17 - Mapa 18 - Resenha 19 - Patente 20 - Norma técnica 21 - Desenho técnico 22 - Ata de reuniões 23 - Atlas 24 - Fotografia aérea 25 - Imagem de satélite 26 - Disco de vinil 27 - CD aúdio 28 - Microfilmes 29 - Microfichas 30 - Transparências 31 - Fax 32 - Selo 33 - Catálogo 34 - Manual 35 - Norma jurídica 36 - Trabalho de conclusão de curso |
| 4 | CODGRUPOPUBLIC | Código do grupo de publicação | Sim | Inteiro | Ver tabela LGRUPOPUBLIC (referência 4) |
| 5 | TITULOORIGINAL | Título original | Não | Texto(200) |  |
| 6 | SUBTITULO | Subtítulo | Não | Texto(200) |  |
| 7 | CLASSIFICACAO | Classificação | Não | Texto(100) |  |
| 8 | SUBCLASSIFICACAO | Subclassificação | Não | Texto(100) |  |
| 9 | COLECAOSERIE | Código da coleção/série à qual pertence a publicação | Não | Inteiro |  |
| 10 | AUTOR | Nome do(s) autor(es) | Não | Texto | Máximo de 150 caracteres para cada nome.  É possível informar o tipo do autor, verifique no final desta página nas observações. |
| 11 | ISBN | ISBN do livro | Não | Texto(20) |  |
| 12 | LOCALPUBLIC | Código do local da publicação | Não | Inteiro | Ver tabela LLOCALPUB (referência 5) |
| 13 | EDITORA | Nome da editora | Não | Texto(50) |  |
| 14 | ANO | Ano de publicação | Não | Inteiro | AAAA |
| 15 | ILUSTRADO | Indica se a obra é ilustrada | Não | Inteiro | 0 - Não ilustrdo 1 - Ilustrado |
| 16 | MATERIALANEXO | Material anexo à publicação | Não | Texto(50) |  |
| 17 | COMENTARIO | Resumo/Observações | Não | Texto(100) |  |
| 18 | IDIOMA | Idioma | Não | Texto(20) |  |
| 19 | DESCRICAOFISICA | Descrição física da publicação | Não | Texto(40) |  |
| 20 | NUMERODEPOSITO | Número do depósito da patente (somente para os tipos de publicação Monografia/Dissertação/Tese) | Não | Texto(20) |  |
| 21 | NUMEROPATENTE | Número da patente (somente para os tipos de publicação Monografia/Dissertação/Tese) | Não | Texto(20) |  |
| 22 | DATADEPOSITO | Data do depósito da patente (somente para os tipos de publicação Monografia/Dissertação/Tese) | Não | Data | DD/MM/AAAA |
| 23 | DATAPRIVILEGIO | Data do privilégio da patente (somente para os tipos de publicação Monografia/Dissertação/Tese) | Não | Data | DD/MM/AAAA |
| 24 | DATACONCESSAO | Data da concessão da patente (somente para os tipos de publicação Monografia/Dissertação/Tese) | Não | Data | DD/MM/AAAA |
| 25 | DURACAO | Duração da fita (somente para o tipo de publicação Fita de vídeo/cassete) | Não | Texto(10) |  |
| 26 | DUBLADOLEGENDADO | Indica se a fita é dublada ou legendada (somente para o tipo de publicação Fita de vídeo/cassete) | Não | Inteiro | 1 - Dublado 2 - Legendado |
| 27 | SISTEMA | Sistema da fita (somente para o tipo de publicação Fita de vídeo/cassete) | Não | Texto(10) |  |
| 28 | MUDO | Indica se a fita não tem som (somente para o tipo de publicação fita de vídeo/cassete) | Não | Inteiro | 0 - Não mudo 1 - Mudo |
| 29 | BITOLADIAMETRO | Diâmetro da bitola da fita (somente para o tipo de publicação fita de vídeo/cassete) | Não | Inteiro |  |
| 30 | ELENCO | Elenco (somente para o tipo de publicação fita de vídeo/cassete) | Não | Texto(255) |  |
| 31 | IDIOMADUBLAGLEGENDA | Idioma de dublagem ou legenda (somente para o tipo de publicação fita de vídeo/cassete) | Não | Texto(20) |  |
| 32 | VELOCIDADEEXECUCAO | Velocidade de execução da fita (somente para o tipo de publicação fita de vídeo/cassete) | Não | Texto(10) |  |
| 33 | MONOSTEREO | Mono/Stereo (somente para o tipo de publicação fita de vídeo/cassete) | Não | Inteiro | 1 - Mono 2 - Stereo |
| 34 | DIMENSAO | Dimensão da fita (somente para o tipo de publicação fita de vídeo/cassete) | Não | Texto(10) |  |
| 35 | FORMAREPRODUCAO | Forma de reprodução da fita (somente para o tipo de publicação fita de vídeo/cassete) | Não | Texto(10) |  |
| 36 | COR | Cor das imagens da fita (somente para o tipo de publicação fita de vídeo/cassete) | Não | Inteiro | 1 - Colorido 2 - Preto e branco |
| 37 | ESCALA | Escala do mapa | Não | Texto(15) |  |
| 38 | MATERIAL | Material da publicação | Não | Texto(10) |  |
| 39 | CLASSIFIC | Classificação complementar | Não | Texto(30) |  |
| 40 | AREACURSODEPTO | Área/Curso/Departamento da publicação | Não | Texto(50) |  |
| 41 | CATEGORIADESC | Descrição da categoria | Não | Texto(200) |  |
| 42 | CODPERIODICIDADE | Código da periodicidade da publicação | Não | Inteiro | Ver tabela LPERIODICIDADE (referência 6) |
| 43 | CODPAIS | Código do país | Não | Inteiro | Ver tabela LPAIS (referência 1) |
| 44 | CODESTADO | Sigla do estado | Não | Texto(2) |  |
| 45 | NIDENTIFICACAO | Número de identificação da publicação | Não | Texto(20) |  |
| 46 | FONTE | Tipo da fonte do artigo | Não | Texto(30) |  |
| 47 | RESPONSAVEL | Responsável/Orientador | Não | Texto(50) |  |
| 48 | ACADEMICO | Acadêmico | Não | Texto(50) |  |
| 49 | GRAUINSTRUCAO | Grau de instrução | Não | Texto(50) | Graduação Mestrado Livre-docência Doutorado Pós-Doutorado Pós-Graduação |
| 50 | EMPRESA | Nome da empresa | Não | Texto(40) |  |
| 51 | AGENCIA | Nome da agência | Não | Texto(40) |  |
| 52 | SECUNDAGEM | Secundagem (usado em fitas) | Não | Texto(20) |  |
| 53 | TIPODOC | Tipo dp documento (artigos de periódico) | Não | Texto(30) |  |
| 54 | TIPODISCO | Tipo do disco (CD, disquete...) | Não | Texto(25) |  |
| 55 | ESPUSADO | Espaço usado pelo disco | Não | Texto(40) |  |
| 56 | ESPLIVRE | Espaço livre do disco | Não | Texto(40) |  |
| 57 | CAPACIDADEMAX | Capacidade máxima do disco | Não | Texto(40) |  |
| 58 | COMPRIMIDO | Indica se o disco está comprimido | Não | Texto(1) | S - Sim N - Não |
| 59 | EMAIL | Endereço de e-mail da publicação | Não | Texto(50) |  |
| 60 | HOMEPAGE | Home-page da publicação | Não | Texto(50) |  |
| 61 | SUPLEMENTO | Suplemento de um periódico | Não | Texto(11) |  |
| 62 | ISSN | ISSN (periódico) | Não | Texto(20) |  |
| 63 | ASSUNTO | Assuntos da publicação | Não | Texto | Máximo de 100 caracteres para cada assunto |
| 64 | CUTTERPHA | CUTTER / PHA da publicação | Não | Texto | Máximo de 20 caracteres para o campo |

   
 **Importante**

**1)** Tabela que receberá as atualizações: LPUBLIC

**2)** Quando a publicação tiver mais de um autor, os nomes dos autores devem vir separados por hífen.

Exemplo: AQUINO, Marcal-REY, Marcos

Observações

Á partir das versões 12.1.23.25, 12.1.24.204 e 12.1.25.135 será possível informar o tipo do autor. O tipo do autor deve ser inserido no final do nome do autor separado pelo carácter "$", sendo que são aceitos somente três tipos:  P - Pessoal, I - Institucional e E - Evento.

Exemplo: Serão cadastrados dois autores, o primeiro sendo evento e o segundo do tipo pessoal (exemplos fictícios).

AQUINO, Marcal**$E**-REY, Marcos**$P**

**3)** Quando a publicação tiver mais de um assunto, as descrições dos assuntos devem vir separadas por hífen.

Exemplo: informática-programação-software

**4)** Em caso de nomes iguais, o sistema utiliza o nome antigo cadastrado no sistema e não duplica o autor e assunto na base de dados.

**5)** Para os casos de publicações com o mesmo título, o sistema irá verificar se o subtítulo, os autores e a editora são diferentes. Se tiver algum dado diferente a importação de todas as publicações será feita. No caso dos dados serem iguais o sistema irá importar a publicação apenas uma vez.

**6)** O campo de código de publicação é opcional e caso não seja informado o sistema irá gerar um código automático na importação. Caso o código informado já exista a publicação não será importada.

Informações

**Código da publicação repetido**: caso seja informado um código de publicação maior que zero (0) e este código já exista no cadastro de publicação, a publicação que se deseja importar não será importada.

**Cadastrar a mesma obra mais de uma vez**: é possível cadastrar uma publicação com mesmo título principal, autores, editora e subtítulo várias vezes, porém com códigos diferentes, neste caso é necessário definir o parâmetro **Permitir cadastro duplicado de publicações (com mesmo título principal, autores, editora e subtítulo),** para mais informações sobre o parâmetro acesse .
