---
content_hash: 31b9afff0a29340c270873c372ee7479363b520cb197629a3c8b571e775cd7d1
fetched_at: '2026-06-29T00:06:01.184960+00:00'
page_id: '198937368'
product: rm
source: tdn-rm
title: ER_vinculacao_de_planilhas_net
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_vinculacao_de_planilhas_net
version: 9
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOP(Totvs Obras e Projetos) |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP007 | **IRM1** | PCREQ-6001 |
| **Requisito1** | PCREQ-6002 | **Subtarefa1** | PDR\_CP\_TOP007-1290 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Migrar as Planilhas RM padronizadas na plataforma Delphi, para a plataforma .Net no modulo de Planilha RM da nova MDI.

## Definição da Regra de Negócio

O Totvs Obras e Projetos com a atualização da versão 12 executando pela nova MDI, tornou-se necessário a migração das Planilhas Eletrônica RM padronizadas do Delphi, para a nova plataforma .Net.

As Planilhas eletrônicas padronizadas do Sistema são:

**BDI do Projeto**

* Planilha eletrônica responsável por auxiliar o calculo do BDI para o Projeto. Nesta planilha são informados algumas taxas como: ISS, Imposto de renda, PIS/CONFINS, EPI entre outras, e a partir destas taxas a planilha possui uma formula de calculo para incluir a sugestão de BDI para o projeto.

**Custo Horário de Equipamentos e Mão de Obra**

* Planilhas eletrônicas responsáveis em auxiliar o calculo de custo hora de um equipamento ou Mão de Obra, com auxilio dos campos livres do TOP. Para cada Insumo do tipo equipamento ou Mão de Obra, o sistema recupera os campos livres informados no cadastro de insumo e calcula o custo produtivo e improdutivo do Equipamento ou Mão de Obra.   
    
  Os campos livres são estruturas definidas na aba de Custo horário do insumo, e a planilha .Net assim como na planilha Delphi, possui as variáveis que poderão ser utilizadas no contexto durante o calculo do Custo Horário.   
  As variáveis na planilha Delphi podem ser acessadas selecionando a célula que clicando com o botão direito do mouse.   
    
    
  As variáveis na Planilha .Net poderão ser acessadas selecionando a célula e acessando o menu variáveis .  
    
    
    
    
  É importante destacar que as variáveis de planilha, só poderão ser utilizadas no calculo de custo hora rio.

**Leis Sociais**

* Esta planilha eletrônica é responsável por auxiliar no calculo do Fator 1  e Fator 2 da Lei Social nos parâmetros de projeto.

**Planilha Padrão Derba**

* O Departamento de Infraestrutura de Transportes da Bahia – DERBA é uma Autarquia do Governo do Estado da Bahia criado pela lei Nº 7.314, de 19 de maio de 1998, vinculado à Secretaria de Infraestrutura – Seinfra. Em 17 de abril de 2002 foi sancionada a da Lei nº 8.250, oficializando a Reestruturação do DERBA, devidamente regulamentada pelo Decreto nº 8.271 de 20 de junho de 2002. Apesar de manter a sigla DERBA (antigamente era conhecido como Departamento de Estradas e Rodagens), passou a denominar-se Departamento de Infraestrutura de Transportes da Bahia, incorporando às suas atribuições a construção e a administração dos terminais rodoviários, hidroviários e aeroviários do Estado. É responsável pelo gerenciamento do sistema estadual de transportes que, além das centenas de terminais modais, conta com uma rede de mais de 20.000 km de rodovias estaduais, além de apoiar a conservação dos sistemas municipais, com aproximadamente 90.000 km, distribuídos em uma área de 560.000 km².

Todas as planilhas customizadas ou criadas pelo cliente deverão utilizar o executável MigradorPlan.exe, fornecido pela Framework Totvs.

## Protótipo de Tela

**Protótipo 01 : Planilha do BDI do Projeto**

****Protótipo 02 : Planilha **Custo Horário de Equipamentos e Mão de Obra******

******Protótipo 03 : Planilha de Leis Sociais******

******Protótipo 04 : Planilha DERBA******

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
