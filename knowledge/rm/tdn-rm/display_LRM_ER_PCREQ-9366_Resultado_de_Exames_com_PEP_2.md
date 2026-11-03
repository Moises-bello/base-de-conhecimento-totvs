---
content_hash: 9561a213cc0615af0207fcf973e146ba607cff6569d858c0aa7a882958708e3d
fetched_at: '2026-06-29T00:08:05.385939+00:00'
page_id: '235595079'
product: rm
source: tdn-rm
title: ER_PCREQ-9366_Resultado_de_Exames_com_PEP_2
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-9366_Resultado_de_Exames_com_PEP_2
version: 115
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

# Resultado de Exames com PEP 2.0

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | R\_SAU\_RM\_V12\_1516 | **IRM1** | PCREQ-6791 |
| **Requisito1** | PCREQ-9366 | **Subtarefa1** | SAU\_DEV-2989 |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

Este requisito tem a finalidade de detalhar a disponibilização dos resultados de exames do TOTVS Gestão Hospitalar dentro da aleta Resultados de Exames do PEP 2.0. Todos os resultados visualizados dentro do sistema serão exibidos no PEP 2.0

### (Obrigatório)

## Definição da Regra de Negócio

 Implementar um serviço que disponibilizará o resultado do exame no  PEP 2.0.

No preenchimento da classe de Wrapper que é utilizado pelo PEP, ao receber o parâmetro com o código do paciente, listar todos os exames do mesmo. Para cada exame o sistema deve montar uma URL que chamará o serviço responsável pela exibição do resultado do exame. Como o TOTVS Gestão Hospitalar possui uma série de integração com outros sistemas laboratoriais, é necessário buscar os dados dos resultados para cada tipo de integração.

Para a montagem da URL, deve-se criar um parâmetro no sistema para armazenar o endereço do TBC que servirá como base para o serviço desenvolvido.

O serviço é responsável por tratar cada integração, sendo assim, pelo número do pedido, deve-se encontrar a unidade de atendimento do exame e verificar a existência de integração. Se não existir, o resultado do exame será gerado com base no relatório do RM Report parametrizado no próprio exame ou no parâmetro geral relacionado à cada tipo de exame (laboratorial ou imagem). Caso esteja configurado uma integração, o arquivo com o resultado estará armazenado no banco de dados ou num diretório. 

Após descobrir onde o resultado se encontra, deve-se gerar o relatório correspondente ou buscá-lo no local correto e enviar o arquivo para o PEP.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
