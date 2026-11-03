---
content_hash: 4fdea90419a9e74a6a24db71c10bb6b7060980b1da4660e0053c9eec1f52d6a5
fetched_at: '2026-06-29T00:09:34.611687+00:00'
page_id: '425459204'
product: rm
source: tdn-rm
title: Linha RM x TOTVS By You ECM (GED) - Configurações e Parâmetros Linha RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459204
version: 6
---

**Configurações e Parâmetros Linha RM**

---

A configuração da integração no Corpore RM é realizada em duas etapas:   
    
 **1. TOTVS Business Connect (TBC)**  
    
 Configurar a integração nos parâmetros do TBC.   
    
 Acesse: Integração | Ferramentas | Parâmetros| Linha RM x GED ( Gerenciamento Eletrônico de Documentos)  
    
 Nesta etapa da configuração devem ser informados os dados referentes ao ECM e estabelcer uma conexão com o mesmo. É possível testar a conexão para verificar se a mesma foi bem sucedida.  
    
 Os dados a serem informados são:

* **Servidor:** onde o GED foi instalado.
* **Porta:** por padrão é 8080. Caso haja alteração, informe a porta onde o GED foi instalado.
* **Usuário:** informe usuário cadastrado no GED, com perfil de administrador.
* **Senha:** informe a senha do usuário (mesma do GED).
* **Empresa:** código informado na instalação. Por padrão é 1.
* **Parâmetros para Visão Padrão:** Ativa Fluxo de Aprovação e Ativa Certificação Digital (O sistema permite que as duas flags sejam marcadas, as duas flags desmarcadas ou apenas a flag Ativa Fluxo de Aprovação).
* **Grupo de usuários:** O grupo de usuários concede permissão aos usuários que estão contidos nele para a pasta raiz. Pode-se escolher um grupo de usuários existente ou criar um novo. É necessário que dentro do grupo de usuários exista o usuário informado anteriormente.
* **Monitor da Fila de Integração - Tipo Log**: Erro, Erro e Alertas ou Trace.

**2. Gerenciar**  
    
 Para realizar o upload de arquivos é necessário realizar uma configuração prévia, na visão de onde os arquivos serão enviados.   
    
 Acesse: Anexos | GED | Gerenciar.  
    
 Nesta etapa deve ser selecionado o GED - ECM, e após definir em qual pasta do ECM os arquivos da visão serão postados:

* Pasta mapeada: é apresentada a estrutura de pastas pré-definida no ECM, devendo ser escolhida uma pasta específica onde o sistema deverá postar os documentos
* Sub-pasta da pasta mapeada: é apresentada a estrutura de pastas pré-definida no ECM, deve-se escolher uma pasta inicial, a partir da qual o sistema deverá postar os documentos. Ao selecionar o arquivo para upload serão apresentadas as sub-pastas da pasta escolhida, para que seja seleciona em qual o arquivo deverá ser postado.
* Retorno de uma coluna do DataServer como nome da pasta: é apresentada a estrutura de pastas pré-definida no ECM, onde deve ser escolhida uma pasta inicial. Após são apresentadas as colunas que existem na visão que está sendo configurada, devendo ser escolhida uma delas. Ao realizar o upload, o sistema irá criar uma pasta com o nome do retorno da coluna selecionada, e o arquivo será postado dentro da pasta. Caso já exista uma pasta com esse nome, o arquivo será postado dentro dela.

Sempre que for um arquivo for enviado, o mesmo será postado no ECM conforme a parametrização da visão. Para que o arquivo seja postado em outra pasta, é necessário realizar a configuração prévia da visão novamente.

---
