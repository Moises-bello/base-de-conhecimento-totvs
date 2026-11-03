---
content_hash: ae6f80ee0ae68af1ac52620e1a95f56f1f7e79052ccad648224a5cc8c672ccaa
fetched_at: '2026-06-29T00:10:26.980748+00:00'
page_id: '515691276'
product: rm
source: tdn-rm
title: Meu Imóvel - Documentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=515691276
version: 19
---

# **1) Introdução**

---

Nesta página o usuário terá à disposição informações referentes aos Informes, Relatórios e Contratos e caso tenha mais de uma Unidade / Contrato de aluguel vinculada ao Cliente/Fornecedor o usuário terá a opção de selecionar a Unidade / Contrato de aluguel desejado  para exibição dos documentos disponibilizados também para os **Contratos**, e a partir do Release 12.1.2302. também os [documentos dos **Empreendimentos**](https://tdn.totvs.com/display/LRM/Portal+do+Cliente+-+PDC+-+Documentos+-+Portal) destes.

Importante

Os relatórios que possuírem o tipo (Tabela RRPTREPORT, coluna TIPO) listado abaixo, serão exibidos na visão do Meu Imóvel quando o contexto for o contrato de aluguel:

* Relatório de Contrato de Locação -> 1000;
* Relatório de Contrato de Administração -> 1001;
* Relatório de Rescisão de Contrato Locação -> 1016;
* Relatório de Pendencias para Rescisão -> 1017;
* Relatório de Lançamentos Mensais -> 1020

# **2) Funcionalidades**

---

As funcionalidades da tela de documentos, quando acessada via aplicativo Meu Imóvel, são:

* **Abrir Documentos:** Clicando no botão o Documento selecionado irá ser gerado a partir do aplicativo preferido para abertura de arquivos PDF do aparelho.
* **Compartilhar Documentos :** Clicando no ícone de Compartilhar do botão , efetua o download do PDF e permite compartilhar / salvar este arquivo em seu aplicativo de preferência. Por exemplo, enviá-lo por um e-mail via App do Gmail, ou compartilhar com outro contato, através do Whatsapp ou Telegram.

Verifiar documentos de uma determinada Unidade , basta clicar sobre  e selecionar a Unidade desejada que deseja visualizar o documento.

**Observações:**

* Para os contratos com Documentos em situação "Inativo" não será habilitado as opções de visualizar ou compartilhar

Não Habilita o compartilhamento do documento.

* Caso não exista nenhum tipo de documento (Informes, Relatórios ou Contratos), será exibida uma tela informando a não disponibilidade de documentos conforme imagem abaixo:

# **3) Anexo de documentos de aluguel**

---

A partir da versão 12.1.29, com a disponibilização dos [anexos de documentos de aluguel](https://tdn.totvs.com/pages/releaseview.action?pageId=549495253) o Meu Imóvel passa a exibir também estes documentos no aplicativo, seguindo toda a lógica já mostrada acima. Para que estes documentos sejam mostrados, os seguintes critérios sejam seguidos:

* Vigência do controle de documentação associado: O Meu Imóvel somente irá mostrar os documentos cujo período vigência não esteja expirado;
* Opção "Publicar" marcada no documento anexo.

**4) Documentos do TOTVS Assinatura Eletrônica**

---

A partir da versão 12.1.33, com a disponibilização da integração com o TOTVS Assinatura eletrônica, todos os documentos associados à contratos de venda ou de aluguel, que foram enviados ao TOTVS Assinatura Eletrônica, poderão ser vistos no menu de documentos, como qualquer outro documento associado aos contratos.
