---
content_hash: fb55e74b3557f3f3f2ba24d16cce8a95f3aa269b6cf43fee604d5fc09fd1f87f
fetched_at: '2026-06-29T00:11:33.255521+00:00'
page_id: '754942624'
product: rm
source: tdn-rm
title: Integração Dr. Tis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=754942624
version: 13
---

## **Conteúdo**

1. **Visão Geral**
2. **Configuração da Unidade de Atendimento**
3. **Configuração dos Endereços de Envio e Recuperação de Laudos Integrados**
4. **Configuração de Usuário Autorizado Junto ao Dr. Tis**
5. **Configurar o Exame com DICOM**
6. **Realizar a Integração de Exames de Imagem**
7. **Obter Resultado de Exames Laudados na Dr. Tis**

itensVisão Geral

## **01. VISÃO GERAL**

Esse documento irá demostrar a configuração do TOTVS Saúde para realização de integração de exames com a Dr. Tis

Configuração da Unidade de Atendimento

## **02.****CONFIGURAÇÃO DA UNIDADE DE ATENDIMENTO**

 1.Selecionar a unidade de atendimento para realizar a configuração na aba de integrações acessando o caminho **Cadastros > Unidade de Atendimento**clicar no botão editar do registro.

2. Selecionar a aba Integrações e na opção de Diagnóstico por Imagem selecionar a opção DrTis.

Configuração dos endereços de envio e recuperação de laudos integrados

## **03.** **Configuração dos endereços de envio e recuperação de laudos integrados**

Além de atribuir o Dr Tis na unidade de atendimento é necessário também realizar a configuração dos endereços de envio. Essa configuração deve se realizada nos **Opções > Parâmetros >** **Parâmetros Gerais > Unidade Diagnóstico** no RMSaude**.**

**Obs:**A DrTis possuí url de integração diferentes a depender da versão contratada como indicado abaixo.

* Clientes que adquiriram a plataforma DrTis até 31/12/2024:  
  <https://docs.app.drtis.com.br/#/>
* Clientes que adquiriram a partir de 01/01/2025:  
  <https://docs.pacs.drtis.com/#/>

Dessa forma, cada cliente deve seguir a documentação correspondente à sua versão/contratação.

Em resumo até a presente data (16/04/2026) os clientes que adiquiriram a DrTis até 31/12/2024 deve utilizar as url's:

* Endpoint Serverless: <https://serverless-api.portal.drnuvem.com.br/v1/>
* WorkList : [https://worklist-api.portal.drnuvem.com.br](https://worklist-api.portal.drnuvem.com.br/)/
* Endpoint Automatização: <https://serverless-api.portal.drnuvem.com.br/v1/>

Os que adiquiriram a partir de 01/01/2025

* Endpoint Serverless: <https://serverless-api.pacs.drtis.com/>
* WorkList : <https://worklist-api.pacs.drtis.com/>
* Endpoint Automatização: <https://serverless-api.pacs.drtis.com/>

Vide que a melhor forma de saber é sempre pedir que o cliente confirme a url que deve utilizar junto a DrTis para não haver erros.

Configuração de Usuário Autorizado Junto ao Dr. Tis

## **04. CONFIGURAÇÃO DE USUÁRIO AUTORIZADO JUNTO A DR TIS.**

Após as configurações padrões para o RM, configurar o usuário que possui cadastro a Dr. Tis em **Cadastro > Prestador.**

É necessário que o cadastro do usuário da Dr Tis seja feito no prestador correspondente ao usuário do RM utilizado.

Selecione o usuário desejado e vai em **Anexo > Endereço de envio prestador.**

Selecione o usuário desejado e vai em **Anexo > Endereço de envio prestador.**Preencha com as informações recebidas pela Dr. Tis em relação ao usuário, senha e chave de acesso. As configurações de Layout e Tipo são padrões conforme abaixo.

Configurar o Exame com DICOM

## **05. CONFIGURAR O EXAME COM DICOM**

Os exames que serão integrados com Dr. Tis devem conter configurado a modalidade DICOM em **Exames e Serviços.**

Com essas configurações o sistema está apto para realizar o envio de exames de imagem ao Dr.Tis

Realizar a Integração de Exames de Imagem

## **06.** **REALIZAR A INTEGRAÇÃO DE EXAMES DE IMAGEM**

Selecione a unidade configurar com Dr Tis para solicitar o pedido de exame e após selecione o exame que foi configurado com DICOM e clique em Salvar ou OK

Se a conexão for realizada o exame será enviado e a tela de exames irá exibir uma mensagem de sucesso na integração.

 Que pode ser validado no Monitor de integrações em **Utilitários > Integração Monitor**  
Com as informações a abaixo: ENVIO\_[NºPEDIDO]; processado e true - para integrações que foram processadas e enviadas a Dr.Tis

Caso durante a integração ocorra algum erro é possível reenviar a mesma seguindo os passos abaixo. Selecionando o exame que não obteve sucesso na integração

Obter Resultado de Exames Laudados na Dr. TIs

## **07. OBTER RESULTADO DE EXAMES LAUDADOS NA DR TIS**

Acesse a central de laudos com usuário configurado e habilitado para obter laudos pela Dr.Tis, selecione o exame com status D (Em digitação) e clique em selecionar.

Se houver resultado de exame junto a Dr. Tis o sistema irá exibir o resultado, atualizar o status da C (Digitação concluída)   
Quando a Dr.Tis tiver disponibilizado a imagem do exame o botão "Abrir PACS" ficará habilitado, com a informação a frente "Imagem disponível" caso contrario o botão ficará desabilitado com a informação de "Imagem indisponível"

Será possível digitar o laudo na central de laudos somente quando o exame estiver com status D (Em digitação), nesse momento o sistema não irá trazer o resultado da Dr. Tis - Salvo quando o laudo for digitado na Dr. Tis.
