---
content_hash: 3c0c8f31350ec39aa9498bc9617972188b1332708a5547486f0407daeb59b03e
fetched_at: '2026-06-28T21:35:16.849906+00:00'
page_id: '1005894967'
product: fluig
source: tdn-fluig
title: Como salvar Imagens e Vídeos locais em formulários usando o componente FLUIGC.richeditor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1005894967
version: 8
---

## Introdução

Este documento tem como objetivo descrever o funcionamento do processo de upload e armazenamento de arquivos no **ECM** a partir de arquivos locais inseridos no FLUIGC.richeditor. O procedimento ocorre de forma automática, atualizando o conteúdo do editor com os novos endereços dos arquivos publicados.

Atenção!

Essa documentação é compatível somente com a release 2.0.0 do Fluig ou superior.

## Exemplos completos para download



## Estrutura básica

O fluxo é composto por três partes principais:

* **Callbacks do editor** (localImageCallback e localVideoCallback).
* **Salvamento e substituição** (saveFilesECM).
* **Upload no ECM** (uploadFileECM).

### Callbacks do Editor

jsRDark

#### localImageCallback

**Objetivo:** Processar imagens inseridas no editor.

1. Recebe a lista de imagens (images).
2. Chama saveFilesECM com o seletor 'img'.
3. Atualiza o conteúdo do editor.

#### **localVideoCallback**

**Objetivo:** Processar vídeos inseridos no editor.

1. Recebe a lista de imagens (videos).
2. Chama saveFilesECM com o seletor 'source'.
3. Atualiza o conteúdo do editor.

### ****Salvamento e substituição****

#### **saveFilesECM**

jsRDark {
const idx = target.src.indexOf('/webdesk');
const normalizedFileUrl = encodeURI(fileUrl);
if (idx >= 0 && target.src.substring(idx) === normalizedFileUrl) {
target.src = newUrl;
}
});
} catch (error) {
console.error('Erro ao processar arquivo:', error);
}
}
return doc.body.innerHTML;
}]]>

**Responsabilidade:** Processar cada arquivo, publicar no ECM e atualizar a URL no HTML.

**Passos:**

1. Obter o HTML do editor.
2. Converter em objeto manipulável via DOMParser.
3. Definir pasta de destino (parentId).
4. Para cada arquivo, publicar no ECM e substituir a URL no HTML.
5. Retornar HTML atualizado.

### **Upload no ECM**

#### **uploadFileECM**

jsRDark {
$.ajax({
type: 'POST',
dataType: 'json',
url: '/content-management/api/v2/documents/publish',
contentType: 'application/json',
data: JSON.stringify(data),
success: data => resolve(data),
error: (xhr, status, err) => reject(err)
});
});
}]]>

**Responsabilidade:** Publicar o arquivo no ECM e retornar o documentId.

**Detalhes:**

* Recebe o nome do arquivo e a pasta de destino.
* Monta objeto com dados do documento.
* Envia requisição para /content-management/api/v2/documents/publish.
* Retorna os dados do documento publicado.

## Observação Importante

Os arquivos são enviados e salvos no ECM **imediatamente** após sua inserção no editor, durante o processo de upload. Este envio **não depende** do salvamento do formulário. Assim, mesmo que o formulário não seja salvo, o arquivo permanecerá publicado no ECM.

## Fluxo Geral

1. Usuário insere imagem/vídeo no editor.
2. Callback (localImageCallback ou localVideoCallback) é acionado.
3. saveFilesECM processa o arquivo:

* Publica no ECM (uploadFileECM).
* Atualiza a URL no HTML.

4. Editor é atualizado com o novo conteúdo.

## Esconder ações de imagens e vídeos locais

Caso queira esconder as ações de imagens e vídeos locais, pode-se usar a propriedade **hideLocalImageAndVideoButton: true** nas configurações do componente.

Exemplo:

jsRDark
