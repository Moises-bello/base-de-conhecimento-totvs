---
content_hash: ed058979ecbd8cdce665e717f311a753d013e116c1549a0e218c87e1e3fd20ed
fetched_at: '2026-06-29T00:08:39.952824+00:00'
page_id: '286026401'
product: rm
source: tdn-rm
title: Novo Conceito - Conexão de Origem Arquivo XML
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286026401
version: 42
---

# Índice:

---

.\*ndice:

# Objetivo:

---

   O objetivo deste documento é mostrar como é feita a configuração de um novo conceito utilizando uma conexão de arquivo XML.

# Introdução:

---

   No TOTVS Business Conector, o Conceito é a estrutura responsável por armazenar os dados de conexões dos sistemas de origem e destino. Uma Conexão Origem ou Destino pode ser de vários tipos, Neste caso será demonstrado como configurar uma conexão do tipo "Arquivo XML".

# Configuração:

---

**Processo de Instalação:**

falseObservação:

O XML utilizado como exemplo contem dados da tabela "GlbUsuarioAction", neste exemplo está sendo feita a importação de um novo usuário para o RM.

false.1º Passo:

Inclua um novo conceito e crie uma nova Conexão de Origem do tipo Arquivo XML. Feito isso preencha o campo "Nome", e em seguida no campo "Arquivo" selecione o "Arquivo XML (Gerado através da ferramenta )" que será utilizado.

falseObservação:

O arquivo XML deve estar uma pasta compartilhada, evitando possíveis erros de configuração.

Após selecionar o arquivo, deve-se marcar os nós do XML, que serão utilizados como tabelas. Imagem demostrativa abaixo:

|  |  |
| --- | --- |

2º Passo:

       Após incluir a Conexão de Origem, crie uma Conexão de Destino do tipo "Data Server RM.NET (neste exemplo será usado esse tipo de conexão, pois esta sendo feita uma importação de dados para dentro do RM)", feito isso preencha o campo "Nome", clique no Lookup do campo "Servidor" e pesquise pela Action "GlbUsuarioAction".

falseObservação:

É necessário Marcar a opção "Permitir Atualização dos Registros" para que os registros da tabela sejam atualizados.

|  |
| --- |

* **Permitir atualização dos registros -** Atualiza os registros.
* **Permitir a exclusão dos registros -** Permiti a exclusão de registros duplicados (é feita a exclusão do registro da tabela de Destino e importado o registro da tabela de Origem).
* **Continuar execução em caso de erros -** O conceito é executado normalmente mesmo quando o mesmo possui erros.
* **Registros por transação -** Permite que seja escolhido quantos registros serão executados por vez.

3º Passo:

   Após a criação das tabelas de Origem e Destino, acesse a aba "Ligações" e arraste a tabela "GUSUARIO" da conexão de Destino, em seguida arraste a tabela "GUSUARIO" da conexão de Origem para dentro da tabela de Destino.

|  |  |
| --- | --- |

Em seguida faça as ligações dos campos da tabela Origem com os campos da tabela de Destino (Imagem demostrativa abaixo):

|  |  |
| --- | --- |

Feito as ligações, clique em "Opções da Ligação" e adicione uma "Chave", em seguida adicione na mesma a coluna "CODUSUARIO (Chave Primária)":

|  |
| --- |

4º Passo:

É necessário criar uma senha para o usuário, para isso arraste um "Valor Fixo" para o campo senha e crie o valor como solicitado:

|  |  |
| --- | --- |

5º Passo:

Salve o conceito e volte a visão principal, em seguida marque o conceito criado e clique em "Processo | Processar Novo Concetio". O conceito será executado corretamente.

|  |  |
| --- | --- |

Não devem ser usados caminhos de arquivo referentes a **unidades de rede mapeadas**. Deve ser usado o caminho do arquivo local em ambiente local e o caminho de rede nos ambientes distribuídos.

Em ambientes **tenantizados**. Deve ser usado o caminho relativo, do arquivo ou diretório.  
*Lembrando que o arquivo ou diretório selecionado deve existir no local indicado dentro da estrutura do tenant.*

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Conexão de Origem Arquivo XML

falsefalse

**Status:** Finalizado

false

**Data:** 10/08/2017

false

**Autores:**
