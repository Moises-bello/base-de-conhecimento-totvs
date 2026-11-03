---
article_id: 360029125611
category: CRM - Dúvidas Gerais
content_hash: f22c8da5e2768e677c5db01010932e6b8e8fa04b913aa65582a2ebd8a2c7e704
fetched_at: '2026-06-28T22:40:27.484176+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Modelos (FATA620 - SIGACRM)
type: support-article
updated_at: '2024-04-25T12:15:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029125611-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Modelos-FATA620-SIGACRM
---

**Dúvida**  
Como cadastrar um modelo no CRM?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da release 12  
  
**Solução**

Esta rotina permite cadastrar um modelo utilizando a associação dos vários componentes que foram incluídos anteriormente.

Seu objetivo é possibilitar a impressão de documentos com a utilização da integração com o Word.

Desta forma, oferece a flexibilidade para que o próprio usuário desenvolva os layouts e informações que neles devem ser impressas. É possível também criar os documentos para os diversos idiomas e países.

**Procedimentos para Cadastrar um Modelo**

1. Em Cadastro de Modelo, selecione a opção incluir.

O sistema apresenta a tela de inclusão.

2. Cadastre o vendedor e as regras a ele vinculadas.

3. Campos que compõem o cabeçalho:

Código: código do modelo (sequência automática);  
Modelo: Descrição/nome do modelo.

4. Campos que compõem os itens de tela:

Ordem: ordem de impressão do componente.  
Componente Principal: código do componente principal (capítulo).  
Descrição do componente: nome do componente.  
Componente Associado: código do componente associado (texto).  
Descrição do componente: nome do componente.

5. Confirme a associação que foi incluída.

**Importante:**

Se o componente é obrigatório ou não, se for igual a **não** ele será um componente opcional e sua seleção será realizada  na tela de seleção e impressão e seleção documentos.

**Procedimento para Exportar Modelos**

1. Na página inicial com os modelos cadastrados, selecione Alterar.  
2. Marque todos os modelos que se quer exportar;  
3. Acesse Outras Ações / Exporta Modelo.  
4 .Na próxima tela selecione a pasta, local onde estão os arquivos que se quer exportar;  
5 .Lembrando que depende da configuração feita no parâmetro **MV\_DOCAR**;  
6. Selecione o arquivo ou arquivos e confirme;  
7. Visualize na próxima tela a confirmação da exportação.

**Procedimento para Importar Modelos**

1. Tal como fizemos na exportação, estando na rotina selecione Alterar;  
2. Marque todos os modelos que se quer importar;  
3. Acesse Outras Ações / Importa Modelo;  
4. Na próxima tela selecione a pasta de origem, local onde estão os arquivos que se quer improtar  
5. Lembrando que depende da configuração feita no parâmetro MV\_DOCAR;  
6. Selecione o arquivo ou arquivos e confirme;  
7. Feito isto visualize na próxima tela a confirmação da importação.

**Veja Também**

**[FAT0081 Configuração de Integração Word (Impressão da Proposta) Oportunidade Vendas](http://tdn.totvs.com/pages/releaseview.action?pageId=239035266)**
