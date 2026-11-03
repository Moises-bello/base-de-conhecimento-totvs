---
content_hash: 136a248fc117c44410a11f71864793a8b2dc06ef10bff6ae85f6986300b966c6
fetched_at: '2026-06-29T00:11:55.018072+00:00'
page_id: '860229308'
product: rm
source: tdn-rm
title: Formatar Datas
type: documentation
url: https://tdn.totvs.com/display/LRM/Formatar+Datas
version: 3
---

Quando precisar formatar datas no arquivo XAML.

Formato exemplo de retorno: "30/07/2024 - 08:51"

## Guia passo a passo

No XAML usando *Converter*:

1. Adicionar o nome do espaço:
   1. xmlns:converters="clr-namespace:RM.Lib.Maui.Converters;assembly=RM.Lib.Maui"
2. Crie o Resources
   1. <ContentPage.Resources>  
        <ResourceDictionary>  
          <converters:DateTimeFormatter x:Key="DateTimeFormatter" />  
        </ResourceDictionary>  
      </ContentPage.Resources>
3. Adicione o *converter* no *binding:*
   1. *<Span Text="{Binding Source={x:Reference page}, Path=DataDescarga, Converter={StaticResource DateTimeFormatter}}" />*

Existe também o ConvertBack que faz o processo ao contrário, retornando um Datetime.

## Mais informações

[Para ver exemplo de utilização acesse a classe de teste da LIB-MAUI.](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/lib-maui?path=/RM.Lib.Maui.Tests/Converters/DateTimeFormatterTest.cs)
