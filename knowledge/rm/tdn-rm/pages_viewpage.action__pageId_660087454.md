---
content_hash: 71539c9e180950ca1dcdb068186fccfb83ba137df228da53b8893c4dab959e63
fetched_at: '2026-06-29T00:11:13.384069+00:00'
page_id: '660087454'
product: rm
source: tdn-rm
title: RPT00003.4 - Exportação/Geração para Imagem
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=660087454
version: 2
---

# Índice:

---

.\*ndice:

# Objetivo:

---

      O objetivo deste documento é exemplificar as possibilidades existentes na exportação de relatórios para imagens.

# Descrição:

---

      Atualmente, é possível exportar um relatório como imagem de duas formas:

* Por meio de "***Processos | Gerar Relatório | Exportação Para Arquivo***", onde é exportado um arquivo JPEG referente ao relatório
* Caso seja necessária mais opções, é possível após a geração do relatório ("***Processos | Gerar Relatório | Apenas Geração***"), através da aba "Visualização da Impressão" e "Exportar Para".

# Exportação Rápida - JPEG:

---

     Caso seja necessário exportar rapidamente um relatório para uma imagem, é possível realizar essa exportação seguindo os passos abaixo:

falseIProcessos → Gerar Relatório

Após selecionar o relatório desejado, acesse Processos → Gerar Relatório, ou aperte **CTRL + G**

Exportação para Arquivo

Marque Exportação para Arquivo

Exportação para Arquivo

Selecione o *Tipo de Saída***Imagem (JPEG)**e siga com a exportação.

Importante

Este modo de exportação **NÃO** exporta marcas d'água, por se tratar de uma exportação rápida. Para exportar marcas d'água, siga a seção **Exportação - Imagem**

# Exportação - Imagem:

---

     Caso deseje exportar seu relatório para outros formatos ou ter um controle maior acerca da exportação do relatório, é possível exportar com diferentes parâmetros, seguindo as informações abaixo:

falseIProcessos → Gerar Relatório

Após selecionar o relatório desejado, acesse Processos → Gerar Relatório, ou aperte **CTRL + G**

Marque Apenas Geração:

Avance com a geração. Uma nova aba será aberta no RM.

Arquivo de Imagem

Na aba aberta, acesse: **Visualização de Impressão → Exportar Para → Arquivo de Imagem**

Opções de Exportação de Imagem

Agora basta realizar as configurações desejadas e clicar em OK para exportar o relatório:

Opções de Exportação de Imagem

* ***Formato de Imagem***: A extensão na qual a imagem será exportada, podendo ser **BMP, EMF, WMF, GIF, JPEG, PNG** e **TIFF**
* ***Resolução (dpi)***: A densidade da imagem (definida em pontos por polegada)
* ***Modo de Exportação:***Como o relatório deve ser exportados. Atenção pois ferramentas especiais como marcas d'água só funcionam ao alterar essa opção.
  + **Arquivo Único:**Irá exportar todo o conteúdo do relatório em um arquivo único, do tamanho mais comprimido possível entre controles. Marcas d'agua não são exportadas nesse modo.
  + **Arquivo Único página-à-página**: Irá exportar todo o conteúdo do relatório em um arquivo único, respeitando o tamanho das páginas. As marcas d'água são exportadas nesse modo.
  + **Arquivos Diferentes**: O relatório será exportado em arquivos diferentes, divididos por página. As marcas d'água são exportadas nesse modo.
* **Faixa de Páginas:**Determina quais páginas deverão ser exportadas. Só é ativada no Modo de Exportação **Arquivo Único página-a-página** e **Arquivos Diferentes**
* **Cor da Borda de Página:**Determina a cor da borda da página.
* Largura da Borda de página: Largura que terá a borda da página. Só é ativada no Modo de Exportação **Arquivo Único página-a-página** e **Arquivos Diferentes**
falsefalse

**Produto:** Framework

false

**Versão:** 12.1.20 ou Superiores

false

**Processo:** Exportação de Relatórios para Imagens

falsefalse

**Status:** Finalizado

false

**Data:** 12/01/2021

false

**Autores:**
