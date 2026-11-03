---
content_hash: 49cc4946ea07c9e0541bba4aa98e34ee89e0fee48d84c28764dcf071c889147c
fetched_at: '2026-06-28T21:35:27.612356+00:00'
page_id: '559498199'
product: fluig
source: tdn-fluig
title: Android - Como utilizar os componentes Leitura de código de barras e QR Code?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=559498199
version: 21
---

# Índice

trueÍndicenone

## Objetivo

O objetivo deste guia é orientar o usuário a como utilizar os componentes Leitura de código de barras e o componente de leitura de QR Code em um formulário de workflow no My Fluig, bem como suas configurações e uso.

O componente de **leitura de código de barras** possui suporte as codificações 128C / GS1-128 / UCC/EAN-128 e EAN-13. E pode ser implementado ao formulário através do Fluig Studio.

Os passos e métodos abaixo podem ser usados tanto na implementação do componente de leitura de código de barras quanto para o componente de leitura de QR Code.

### Criando um formulário

---

 **01.** O primeiro passo será criar um formulário via fluig Studio, para isso basta seguir atentamente os passos das documentações [Fluig Studio](https://tdn.totvs.com/x/oxVbB) e [Desenvolvimento de formulários](https://tdn.totvs.com/x/U4l8B).

Pode ser interessante fazer a leitura das documentações [Configuração para uso inicial](https://tdn.totvs.com/x/FQxFCg)

[do Fluig Studio](https://tdn.totvs.com/x/FQxFCg) e [Guia de atualização Fluig Studio](https://tdn.totvs.com/x/76tSDg) para garantir seu correto funcionamento e garantir uma boa experiência.

**02.** Implementar o componente Leitura de código de barras ou o componente de leitura de QR Code no desenvolvimento do formulário.

### Funcionamento do componente

---

Os componentes de leitura do código de barras e leitura de QR Code se baseiam em **2 métodos** que devem ser incluídos dentro de uma tag **<script>** no formulário a ser usado.

* Esta função é interceptada nativamente pelo aplicativo e inicia a captura do código de barras ou QR Code via câmera.

Método 1

* Esta função é chamada pelo aplicativo para devolver para o formulário o valor lido pela câmera.

Método 2

### Confira na prática

---

sample1Recurso em uso - Leitor de código de barras

* Assim que a câmera lê o código de barras o valor correspondente ao código é enviado ao *input* do campo do formulário em questão.

sample1Recurso em uso - Leitor de QRCode

* Assim que a câmera lê o código de barras o valor correspondente ao código é enviado ao *input* do campo do formulário em questão.

300

#### Exemplo de uso

---

O exemplo abaixo pode ser utilizado para a implementação do componente de código de barras, quanto o componente de leitura de QR Code.

Produto
