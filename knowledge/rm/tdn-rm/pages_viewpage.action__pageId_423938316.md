---
content_hash: 726523668c0959da7b99f9102eb7e97aa476c3225f6b1cab00021e7a589ff27a
fetched_at: '2026-06-29T00:09:26.539068+00:00'
page_id: '423938316'
product: rm
source: tdn-rm
title: Layout de Inventário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938316
version: 2
---

Neste módulo você poderá criar, alterar e excluir diversos layout's para serem utilizados na importação de inventário.  
Na maioria das vezes será necessário criar apenas um layout, que deverá ser compatível com o layout do seu coletor de dados, para que o sistema possa fazer a importação do inventário corretamente. Mas caso você utilize mais de um coletor ou queira criar arquivos exclusivos, poderá criar quantos layout's forem necessários.

O layout a ser criado neste módulo deve obedecer ao layout do leitor ótico, pois ao coletar os dados dos patrimônios da empresa com o leitor, ele criará um arquivo txt com um determinado layout. Será este mesmo arquivo que o Totvs Gestão Patrimonial irá importar para permitir a geração de relatórios de inventário. Dessa forma o layout do arquivo deve ter o mesmo layout cadastrado aqui.  
   
Para criar um Layout, devem ser observadas algumas regras:

**Código:** Na importação do Inventário deverá ser informado o código do cadastro do layout

**Código do Patrimônio, Código de Barras e Código da Filial:** Ao salvar o layout o sistema valida se o Código do Patrimônio ou o Código de Barras estão presentes no layout, a partir destes códigos o sistema irá identificar o registro. Os dois campos também podem ser utilizados juntos no mesmo layout.

O campo Filial será obrigatório quando informado Departamento.

**Campos (Posições e Tamanhos):** O layout permite que sejam informadas até 8 posições.

**Filial-**  Tamanho máximo permitido: 3

**Código de Barras-** Tamanho máximo permitido: 30

**Departamento-** Tamanho máximo permitido: 25

**Localização-** Tamanho máximo permitido: 40

**Centro de Custo-**  Tamanho máximo permitido: 25

**Código do Patrimônio-** Tamanho máximo permitido: 25

**Responsável-** Tamanho máximo permitido:16

**Observação-** Tamanho máximo permitido: 255

**Exemplo de arquivo a ser importado**  
Supondo que o layout a ser utilizado está cadastrado com as seguintes Posições/Tamanhos:

Código: 01 Descrição: Layout para coleta de patrimônios

Posição 1- Filial: 03

Posição 2- Localização: 08

Posição 3- Centro de Custo: 08

Posição 4- Código de Barras: 20

Posição 5- Departamento: 03

Posição 6- Código do Patrimônio: 15

Posição 7- Responsável: 08

Posição 8- Observação: 15

Arquivo Texto:  
Onde estiver hífen leia-se espaço em branco.  
-01------04---1.001-------------0101001-01------01.01.001---00006-----Inventário

Veja Também
