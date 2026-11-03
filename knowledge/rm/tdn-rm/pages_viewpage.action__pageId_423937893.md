---
content_hash: 8532c2c220b0de0ad23165f1239f7ae60029082a0dccfce134831b20908a5924
fetched_at: '2026-06-29T00:09:24.098623+00:00'
page_id: '423937893'
product: rm
source: tdn-rm
title: Integrações Fiscais (Movimento de Repasse - Reinf)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937893
version: 3
---

A primeiro momento, deve-se parametrizar um tipo de movimento cujo código se inicie com 1.2.XX ou 2.2.XX.   
Estando na tela de parametrização do movimento escolhido, navegar até a Etapa 61 - Fiscal - Dados Fiscais, onde poderá ser encontrada a flag 'Movimento de Repasse EFD Reinf', que deve ser habilitada.  
Após o término da parametrização, durante a inclusão/edição de um movimento será exibido o campo de Processos, na aba Integrações | Processos Judiciais. Na visão dos itens, o campo 'Tipo Repasse EFD Reinf' pode ser localizado na aba Integrações | Fiscal.   
Seu conteúdo é disposto em um ComboBox, que possui os seguintes valores:

* Patrocínio;
* Licenc. de marcas e símbolos;
* Publicidade;
* Propaganda;
* Transmissão de espetáculos.

Movimentos que serão utilizados para Repasse, tem como preenchimento obrigatório o campo habilitado na visão de seus itens.   
É importante citar também que cada item somente pode possuir somente um (01) tipo de repasse associado, mas não existe(m) restrição(ões) para associar tipos de repasse repetidos, dentre os itens existentes no movimento.
