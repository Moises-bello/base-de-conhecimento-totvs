---
content_hash: 09a0422121699c2724778885419a90c7486c82a029f1e51e765b3cdab1d2dca9
fetched_at: '2026-06-29T00:12:09.147887+00:00'
page_id: '939253891'
product: rm
source: tdn-rm
title: Telemetria
type: documentation
url: https://tdn.totvs.com/display/LRM/Telemetria
version: 31
---

---

O módulo de Manutenção de Equipamentos do Totvs Construção Obras e Projetos  agora possui a  integração com a tecnologia de telemetria do parceiro News GPS, permitindo, através da coleta de dados de sensores ou dispositivos remotos, a alimentação dos indicadores de uso e índices de acompanhamento dos equipamentos e a geração automática das Ordens de Serviço preventivas ou corretivas necessárias.

Para consultar a documentação de apoio do parceiro [NewsGPS](https://tryvia.com.br/produtos).

Premissas

Para utilizar a integração é necessário:

1 - Permissão de perfil de usuário com acesso a funcionalidade de Telemetria

2 - Parametrizar a integração do Manutenção de Equipamentos com a Telemetria

* Acesse: **Manutenção de Equipamentos > Parâmetros > Telemetria**

**Usuário e senha de acesso utilizados na integração com a Telemetria**

Informar o usuário e senha da interação com [NewsGPS](https://tryvia.com.br/produtos).

**Indicadores de uso dos objetos de manutenção que serão atualizados pelos apontamentos de equipamentos de mobilidade**

Os campos Indicador de uso Quilometragem e Indicador de uso Horímetro serão carregados com base nos indicadores de uso cadastrados nos parâmetros de **Manutenção de Equipamentos do Totvs Construção Obras e Projetos**.

Possibilitam a integração dos [apontamentos de equipamento](https://tdn.totvs.com/display/LRM/Equipamento?draft=true#Equipamento--1033126653) do app **Minha Obra** com o **Manutenção de Equipamentos do Totvs Construção Obras e Projetos.**

Informando os parâmetros de Quilometragem ou Horímetro, os mesmos serão enviados para o histórico de indicadores de uso do objeto de manutenção na execução do processo "Apropriar custo" da visão de apontamentos. Mais detalhes do processo em:[Apropriar custos](https://tdn.totvs.com/display/LRM/Equipamento#Equipamento--113135509)

Para saber mais sobre  **Manutenção de Equipamentos do Totvs Construção Obras e Projetos** clique [aqui](https://tdn.totvs.com/x/OJIiLQ).

Observação

Quando forem informados os **indicadores de quilometragem (km)** e de **horímetro (tempo de funcionamento do equipamento)**

* Cada indicador deve estar associado à **unidade de medida correta**:

  + Para **quilometragem**, o **indicador** deve usar a **unidade base "KM"**;
  + Para **horímetro**, o **indicador** deve usar a **unidade base "H"** (de horas).
Cadastros

É importante que os cadastros abaixo possuam as informações de telemetria para que ao executar o processo de atualização traga as informações.

[Objeto de Manutenção](https://tdn.totvs.com/pages/viewpage.action?pageId=819495796) - Este cadastro possui a aba integrações onde se realiza o vinculo com a Telemetria e possui também o tipo de indicador de uso habilitado.

[Indice de Acompanhamento](https://tdn.totvs.com/pages/viewpage.action?pageId=819495446) - Este cadastro possui uma aba "Telemetria" que vincula a integração.

Indicador de Uso (uma aba do objeto de manutenção ) (Odomêtro e HorÍmetro)

Processos

* [Atualização de dados via Telemetria](https://tdn.totvs.com/pages/viewpage.action?pageId=939254768)
