---
content_hash: d55ff6176a58ae3580337f66b775cf8c9e39887bd9ff72022ee47240966a1198
fetched_at: '2026-06-29T00:09:24.496868+00:00'
page_id: '423937930'
product: rm
source: tdn-rm
title: Movimento de BP-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Movimento+de+BP-e
version: 5
---

Inicialmente, o tipo de movimento escolhido deve ser parametrizado para permitir o relacionamento de um documento cujo Código do Modelo (CODMODDOC) seja 63.   
Para isto, basta navegar até a etapa 63 - Fiscal - Escrituração Fiscal e indicar um Tipo de Documento, seja no campo 'Default' ou em 'Outros Códigos', que possua o código especificado.   
Se o código do tipo de movimento iniciar com 2.X.XX, na etapa 69 - Fis - Conhecimento de Transporte, o valor do campo 'Tipo de Operação do Conhecimento de Transporte' deve ser 'Não Usar CTRC'.   
Caso contrário uma mensagem de consistência será exibida ao tentar salvar a parametrização.  
Ao incluir um novo movimento, que tenha relacionado um Tipo de Documento com o código 63, a aba BP-e deverá ser exibida no grupo Integrações e nela conterá o campo de Chave de Acesso, para ser preenchido com a chave do respectivo BP-e.   
Em movimentos do tipo 2.X.XX, na aba Transporte | Identificação será exibido também o campo Tipo BP-e, que contém os seguintes valores:

* BP-e Normal;
* BP-e Substituição;
* BP-e TM (Transporte Metropolitano).

Este segundo deve ser utilizado sempre que a inclusão de movimento for relacionada a um BP-e de substituição.   
Neste caso, deve ser parametrizado um movimento para utilizar Cópia por Referência, com o motivo 17, e durante a criação deve-se apontar o movimento de BP-e a ser substituído
